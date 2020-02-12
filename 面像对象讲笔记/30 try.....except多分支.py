# Author : Sky 
# @Time : 1/25/20 7:36 下午
# @Site : 
# @File : 30 try.....except多分支.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-
# 多分支：被监测的代码块抛出的异常有多种可能性，并且我们需要针对每一种异常都定制专门的处理罗辑
# try:
#     print('---->1')
#    # name
#     print('----->2')
#     l=[1,2,3]
#     l[100]
#     print('------>3')
#     d={}
#     d['name']
#     print('------->4')
# except NameError as e:
#     print('=====sk',e)
# except IndexError as e:    # 到这里可以一直except 下去，有点像多分支。
#     print('=====>',e)

# 万能异常： Exception ，被监测的代码块抛了的异常有多种可能性，
# 并且我们针对所有的异常类弄都只有一种处理逻辑就可以了，那就使用Exception

#  ！！！ 可以结合 多分支引用。
# try:
#     print('---->1')
#     name
#     print('----->2')
#     l=[1,2,3]
#     l[100]
#     print('------>3')
#     d={}
#     d['name']
#     print('------->4')
# except Exception as e:
#     print('-----',e)
# print('上面错误抛出后还可以往下面走')
#

# 其它结构
# try:
#     print('---->1')
#     # name
#     print('----->2')
#     # l=[1,2,3]
#     # l[100]
#     print('------>3')
#     # d={}
#     d['name']
#     print('------->4')
# except Exception as e:
#     print('-----',e)
# else:
#     print('这是在被监测的代码块没有发生异常时执行')
#
# finally:      # 这个一般在回收资源的时候使用。下面举例
#     print('不管被监测代码块有无发生异常都会执行')
# print('上面错误抛出后还可以往下面走')

# finally的使用场景
# try:
#     f=open('29_a.txt','r',encoding='utf-8')
#     print(id(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))    #这里理论是说在第4行之生就会错了。     v
#     print(next(f))
#     print(next(f))
# finally:                    #加一个这个，我不管这个逻辑出不出错 ，到后面我都关闭。
#     f.close()
#     print('关闭文件',next(f))

# 异常： 主动触发异常： raise 异常类型 值。
# class People:
#     def __init__(self,name,age):
#         if not isinstance(name,str):
#             raise TypeError('名字必须传入STR类型')
#         if not isinstance(age,int):
#             raise TypeError('年龄必须传入INT类型')
#         self.name=name
#         self.age=age
# p=People('sky','18')     #这里我们传入的年龄如果是字符串，会报第二个设定错误

# 断言 assert
# info = {}
# info['name']= 'sky'
# # info['age'] = 18
# # 传统解决方案 加判断
# # if 'name' not in info:
# #     raise KeyError('这里必须要有name这个KEY')
# # if 'age' not in info:
# #     raise KeyError('这里必须要有age这个KEY')
# # 用断言
# assert ('name' in info) and ('age' in info)
# #正常情况下 我们是这样走的，但是不确定有没有name 和 age 这两个key 值。
# if info['name'] == 'sky' and info['age'] > 10:
#     print('welcome')
#
#

# 自定义异常
class MyException(BaseException):
    def __init__(self,msg):
        super(MyException,self).__init__()
        self.msg=msg
        
    def __str__(self):
        return '<%s>' %self.msg
raise MyException('我自己的异常类型')


