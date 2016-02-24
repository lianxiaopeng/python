class Student(object):
	def __init__(self,name):
		self.name = name 
	def __str__(self):
		return 'Student'
	
		
stu = Student("hello")
print(stu)

#裴波那契系数
class Fib(object):
	def __init__ (self):
		self.a , self.b = 0 ,1
	def __iter__(self):
		return self
	def __next__ (self):
		self.a , self.b = self.b , self.a + self.b
		if self.a > 100 :
			raise StopIteration()
		return self.a
	def __getitem__(self,n):
		if isinstance(n,int):
			
			a , b = 0 , 1
			for x in range(n):
				a , b = b ,a + b
			return a
		if isinstance(n,slice):
			start , stop = n.start,n.stop
			if start is None:
				start = 0
			a , b = 0 ,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a , b  =  b , a + b
			return L
		
f1 = Fib()
for f in f1:
	print(f)
print(f1[4])


print(f1[0:4])

#getattr

class Chain(object):
	def __init__(self,param=''):
		self.param = param
	def __getattr__(self,param):
		return Chain('%s/%s' % (self.param,param))
		
	def __str__(self):
		return self.param
		
		
print(Chain("/ss/bb/cc"))
print(Chain().status.user.timeline.lisddddt)