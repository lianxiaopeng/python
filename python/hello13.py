


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
                          
