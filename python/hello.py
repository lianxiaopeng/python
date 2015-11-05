def flip_bit(number,n):
    result = 0b1
    n = n -1 
    while n>0:
        n = n -1
        result<<1
    return bin(number ^ result)
r = flip_bit(0b111,2)
print(r)
        
        



def remove_duplicates(lis):
    if lis==[]:
        return lis
    else:
	    n=[]
	    n.append(lis[0])
    for i in range(len(lis)):
        j=0
        while j<len(n):
        	
            if lis[i]==n[j]:
               
                break
            else:

                
                j = j + 1
        if j == len(n):
        	n.append(lis[i])
    return n

print(remove_duplicates([1,1]))
                          
