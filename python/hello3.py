#循环索引
L = [1,2,3,4]
for i in L:
	print(i)
#切片
print(L[-2:])
#迭代
from collections import Iterable
print(isinstance('ss',Iterable))
print(L[-1:-3])
