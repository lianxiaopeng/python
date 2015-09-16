#生成器
L=[x*x for x in range(10)]
print(L)
G=(x*x for x in range(1,10))
print(G)
print(next(G))
print(next(G))
print('#')
for i in G:
	print(i)


def lxp(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a,b = b , a+b
		n = n + 1
	return 'done'

print(lxp(6))

def lxp1(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b , a+b
		n = n + 1
	return 'done'

G1 = lxp1(6)
for ii in G1:
	print(ii)
try:
	print(next(G1))
except StopIteration as e :
	print("xxx",e.value)

