#类和实例
class Student(object):
	pass
stu = Student()
print(stu)
print(Student)
#给实例绑定变量
stu.name = "hello world!"
print(stu.name)
class Teacher(object):
	def __init__(self):
		pass

	def get_name(self):
		return self.name
	def set_name(self,name):
		self.name = name
	
teach = Teacher()
teach.set_name("lxp")
print(teach.get_name())	

#获取对象的属性和方法
import types
d = dir(types)
print(d)
print(type("") == str)
print(type(1) == int)


import types
import functools
t = dir(types)
print(type(t))
print(dir(functools))