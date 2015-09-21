#使用property
class Student:
	pass
stu = Student()
def set_score(self,score):
	self.score = score
from types import MethodType
stu.set_score = MethodType(set_score,stu)
stu.set_score(100)
print(stu.score)




class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,width):
		self._width = width
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,height):
		self._height = height
	@property	
	def resolution(self):
		return self._width *self. _height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
#assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution