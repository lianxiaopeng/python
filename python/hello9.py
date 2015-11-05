#偏函数
b = int("01011001",base=2)
print(b)
def int2(b) :
	return int(b,base=2)
print(int2("111100"))

#简化调用
import functools
int8 =  functools.partial(int,base=8)
print(int8("71"))
max10 = functools.partial(max,10)
print(max10(5,6,7))
def hello(**kwargs):
    for key , values in kwargs.items():
        print(key,values)
hello(base = 3,dd=3,a33=3)
