#循环索引
L = [1,2,3,4]
for i in L:
	print(i)
#切片
print(L[-2:])
print(L[-1:-3])
print(L[-1:])
print(L[-2:-1])
print(L[-3:-1])
print(L[-3:])
print(L[3:])
print([1,3,5][0:])
#迭代
from collections import Iterable
print(isinstance('ss',Iterable))
print(isinstance(enumerate(['a','b']),Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(range(1,10),Iterable))
print(isinstance(list(range(1,10)),Iterable))

print("迭代end")
print(type(range(1,10)))
l1 = ['a','b','c']
m1 = enumerate(l1)
print(m1)
for x,y in m1:
	print(x,y)

#列表生成式
print(list(range(1,11)))
for x in range(1,11):
	print(x)

print([x * x for x in range(1,11) ])
print([x * x for x in list(range(1,11)) ])
print([x*y for x,y in enumerate(list(range(1,10)))])


