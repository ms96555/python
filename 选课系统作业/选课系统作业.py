# Author : Sky 
# @Time : 1/27/20 11:28 上午
# @Site : 
# @File : 选课系统作业.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
import os
import sys
import pickle

class Course:
    def __init__(self, name, price, period, teacher):
        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher


class Preson:
    def show_courses(self):
        with open('student_select_course/couerse_info', 'rb') as f:
            count = 0
            while True:
                try:
                    count += 1
                    courese_obj = pickle.load(f)
                    print(count, courese_obj.name, courese_obj.price, courese_obj.period, courese_obj.teacher)
                except EOFError:
                    break


class Student(Preson):
    operater_list = [
        ('查看可选的课程', 'show_courses'),
        ('选择课程', 'select_course'),
        ('查看已选的课程', 'check_select_course'),
        ('退出', 'exit')]

    def __init__(self, name):
        self.name = name
        self.courses = []

    def select_course(self):
        self.show_courses()
        num = int(input('num>>:'))
        count = 1
        with open('student_select_course/couerse_info', 'rb') as f:
            while True:
                try:
                    course_obj = pickle.load(f)
                    if count == num:
                        self.courses.append(course_obj)
                        print('您选择了%s课程' % (course_obj.name))
                        break
                    count += 1
                except EOFError:
                    print('没有您选择的课程')
                    break

    def check_select_course(self):
        for course in self.courses:
            print(course.name, course.teacher)

    def exit(self):
        with open('student_select_course/student_info', 'rb') as f1, open('student_select_course/student_info_bak',
                                                                          'wb') as f2:
            while True:
                try:
                    student_obj = pickle.load(f1)
                    if student_obj.name == self.name:
                        pickle.dump(self, f2)
                    else:
                        pickle.dump(student_obj, f2)
                except EOFError:
                    break
        os.remove('student_select_course/student_info')
        os.rename('student_select_course/student_info_bak', 'student_select_course/student_info')
        exit()

    @staticmethod
    def init(name):
        with open('student_select_course/student_info', 'rb') as f:
            while True:
                try:
                    stu_obj = pickle.load(f)
                    if stu_obj.name == name:
                        return stu_obj
                except EOFError:
                    print('没有这个学生')
                    break


class Manager(Preson):
    operater_list = [('创建课程', 'creater_coures'),
                     ('创建学生', 'creater_student'),
                     ('查看所有的课程', 'show_courses'),
                     ('查看所有的学生', 'show_students'),
                     ('查看所有学生的选课情况', 'show_students_courses'),
                     ('退出', 'exit')]

    def __init__(self, name):
        self.name = name

    def creater_coures(self):
        name = input('course name:')
        price = input('course price:')
        period = input('course period:')
        teacher = input('course teacher:')
        course_obj = Course(name, price, period, teacher)
        with open('student_select_course/couerse_info', 'ab') as f:
            pickle.dump(course_obj, f)
        print('%s课程创建成功' % course_obj.name)

    def creater_student(self):
        # 用户名和密码记录到user_info，将学生对像存储在student_info文件
        stu_name = input('student name:')
        stu_pwd = input('student password:')
        stu_auth = '%s|%s|Student\n' % (stu_name, stu_pwd)
        stu_obj = Student(stu_name)
        with open('student_select_course/user_info', 'a', encoding='utf-8') as f:
            f.write(stu_auth)
        with open('student_select_course/student_info', 'ab') as f:
            pickle.dump(stu_obj, f)
        print('%s学生已经创建成功' % stu_obj.name)

    def show_students(self):
        with open('student_select_course/student_info', 'rb') as f:
            count = 0
            while True:
                try:
                    count += 1
                    student_obj = pickle.load(f)
                    print(student_obj.name)
                except EOFError:
                    break

    def show_students_courses(self):
        with open('student_select_course/student_info', 'rb') as f:
            while True:
                try:
                    student_obj = pickle.load(f)
                    course_name = [course.name for course in student_obj.courses]
                    print(student_obj.name, '所选课程%s' % '|'.join(course_name))
                except EOFError:
                    break

    def exit(self):
        exit()

    @classmethod
    def init(cls, name):
        return cls(name)


def login():
    name = input('请输入你的用户名>>: ')
    pawd = input('请输入你的密码>>:')
    with open('student_select_course/user_info', 'r', encoding='utf-8') as f:
        for line in f:
            usr, pwd, identify = line.strip().split('|')
            if usr == name and pawd == pwd:
                return {'result': True, 'name': name, 'id': identify}
        return {'result': False, 'name': name}


ret = login()
if ret['result']:
    print('\033[1;32;40m登录成功\033[0m')
    if hasattr(sys.modules[__name__], ret['id']):
        cls = getattr(sys.modules[__name__], ret['id'])
        obj = cls.init(ret['name'])
        while True:
            for id, item in enumerate(cls.operater_list, 1):
                print(id, item[0])
            fun_str = cls.operater_list[int(input('>>>: ')) - 1][1]
            # print(fun_str)
            if hasattr(obj, fun_str):
                getattr(obj, fun_str)()
    else:
        print('登陆失败')
