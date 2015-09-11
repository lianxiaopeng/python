#用索引取出list指定元素
L = [
 ['Apple', 
 'Google', 'Microsoft'],
 [
 'Java', 'Python', 'Ruby', 'PHP'],
  ['Adam', 'Bart', 'Lisa']
]
#打印Apple
print(L[0][0])
sum = 0
for value in range(5):
	sum = sum + value
print(sum)	

str1 = 'abc'
list1 = ['a','b','c']
tuple1 = ('a','b','c')
dic1 = {'1':'a','2':'b','3':'c'}
set1 = set(list1)
print('str1 = %s' % str1)

print('list1 = %s' % list1)
print(tuple1)
#print('tuple1 = %s' % tuple1[0])
print('1' in dic1)
print('dic1 = %s' % dic1)
print('set1 = %s' % set1)
