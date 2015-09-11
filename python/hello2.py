def function(var1,var2,var3):
	min = 0
	max = 0
	if var1 < var2:
		if var1<var3:
			min = var1
		else: 
			min = var3

	elif var2 < var3:
		min = var2
	else :
		min = var3
	return min,8
	
result = function(5,2,3)
print(result)	

