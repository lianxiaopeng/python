#装饰器作业

import functools
from collections import Iterable
def log(p1):
	#print("log")
	#print(p1)
	
	def log_f1(p1):
		#print("log_f1")
		#print(p1)
		@functools.wraps(p1)
		def log_f2(*args):
			print("log_f2")
			print(args)
			p1()
			return 1
		return log_f2
	
	def log_f3(*args):
		print("log_f3")
		print(args)
		p1()
		return 2
	if isinstance(p1,Iterable):
		return log_f1
	else:
		return log_f3

@log("sss")
def f1():
	print("f1")
@log
def f2():
	print("f1")

#f1 =  log("sss")(f1)
f1("abc")
print(f1.__name__)
f2("cba")
print(f2.__name__)

