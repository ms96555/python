# Author : Sky 
# @Time : 1/28/20 1:55 下午
# @Site : 
# @File : 23 反射.py
# @Software: PyCharm 
# -*- coding: utf-8 -*-

# 反射， 通过字符串映射到对象的属性
# class People:
#     country = 'china'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print('%s is talking' %self.name)
#
# obj = People('egon',18)

# print(obj.name)
#
# print(obj.talk)
#
# choice = input('>>:')
# print(obj.choice)

# hasattr(obj,'name')   #里面有两个， 第一个是你的对像  第二个，字符串形式的的那个属性  这第的意思是判断OBJ里面有没有name 这个属性

#
# print(hasattr(obj,'name'))
# print(hasattr(obj,'talk'))

# getattr()  #里面有三个传数， 第一个是对像， 第二个，字符串形式的的那个属性 , 第三个是默认的属性， 比如 第二个参数是对象里面没的时候，就不会报错，会返回NONE
# print(getattr(obj,'namess',None))

# print(getattr(obj,'talk',None))
#
# setattr(obj,'sex','male') # 它的作用就是 obj.sex = 'male'
# print(obj.sex)

# print(getattr(People,'country'))  #这种方式对类也是适用的，比如我取这个类有没有这个属性

# 反射的应用、
# 这个的作用是 接受用户的输入，触发这个对像下面的某个方法

class Service:
    def run(self):
        while True:
            # cmd = input('>>:').strip()  # 如果说cmd = 'get a.txt'
            inp = input('>>:').strip()
            # cmd,args = inp.split()  # cmd,agrs = ['get','a.txt']
            cmds = inp.split() #也可以这样写，cmds= ['get','a.txt'] 拿到一个列表
            # ！！！ 如果用户传入的不对怎么办，加个判断 ,用刚刚学的hasattr
            if hasattr(self,cmds[0]):  #判断这个输入的值 ，在不在这个对象里面。
                func = getattr(self,cmds[0])  # 有那我们就以取到这个绑定方法。
                func(cmds) # 这个绑定的方法 加括号就可以调用
            else:
                print('没有这个方法')

    def get(self,cmds):
        print('get.......',cmds)

    def put(self):
        print('put.......')
#定义一个类，有个run 方法， 接授用户指令。然后有下载 ，上传， 接着再实例化一个对象

# 这个的作用是 接受用户的输入，触发这个对像下面的某个方法
obj = Service()
obj.run()

# 如果说我要这样下载  get a.txt a.txt这个文件

