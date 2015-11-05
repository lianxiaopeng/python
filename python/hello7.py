#装饰器

import functools
def log(p1):
	#print("log")
	#print(p1)
	def log_f1(p1):
		#print("log_f1")
		#print(p1)
		functools.wraps(p1)
		def log_f2(*args):
			print("log_f2")
			print(args)
			p1()
			return 1
		return log_f2
	return log_f1

@log("sss")
def f1():
	print("f1")

#f1 =  log("sss")(f1)
f1("abc")
print(f1.__name__)

