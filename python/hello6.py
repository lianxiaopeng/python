#按字母排序
from_str = ['zjob','teryy','Zone']
to_str = sorted(from_str,key=str.lower)
print(to_str)
#按名字排序
def _by_name(f):
	a , b = f
	return a.lower()
	pass
L = [('Lxp',88),('dlh',99),('kely',66)]
LL = sorted(L,key=_by_name,reverse=True)
print(LL)
#LL = sorted(L,key=str.lower,reverse=True)
#返回函数
from functools import reduce
def red(a,b):
	return a*b
def a1(*args):
	def a2():
		return reduce(red,args)
	return a2
a3 = a1(1,2,3)
print(a3())

def a4(*args):
	return lambda : reduce(red,args)
a5 = a4(2,3,4)
print(a5())