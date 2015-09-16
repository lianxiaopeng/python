#map()
src = ['snow','jhon','lucy']
def _1st_word_upper(str):
	return str[0:1].upper() + str[1:]
desc = map(_1st_word_upper,src)
for d in desc:
	print(d)
#str to float
def str2float_tmp(p1,p2):
	
	return p1*10 + p2
	
from functools import reduce	
def str2float(str):
	result = reduce(str2float_tmp,[{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x]  for x in str if x != '.'])
	print(result)
	n  = 0
	while n < len(str):
		if(str[n] == '.'):
			
			return result / (10**(len(str)-n-1))
		n = n + 1	
		
	
#print(list(map(str2float,['123.13','234.1'])))

#运算符
#+加法
#-减法
#*乘法
#**幂次
#/除法
#//取整，商的整数部分
#%取余
#&位与
#|位或
#^位异或
#~位翻转 x -> -(x+1)
#<<左移
#>>右移
#3开始的奇数生成器
def odd():
	n = 3
	yield n
	while True :
		n = n + 2
		yield n 

def filter_patern(n):
	return lambda x : x%n > 0  
	
def prime(max):
	n = 3
	tmp = odd()
	print(n)
	while True:
		
		tmp = filter(filter_patern(n),tmp)
		result = next(tmp)
		
		if result >= max:
			break
		print(result)
		n = result
	
prime(10000)
	
	
	
	
	
	
	
	
	
	
	
	
	