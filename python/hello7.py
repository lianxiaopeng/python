#装饰器


def log(p1):
	print("log"+p1)
	def log_f1(p1):
		print("log_f1"+p1)
	return log_f1

@log("sss")
def f1():
	print(f1)

#f1 =  log("sss")(f1)

