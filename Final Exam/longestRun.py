def longestRun(L):
	result=0
	temp=1
	i=0
	while(i<len(L)-1):
		j=i+1
		while j:
			if j<len(L):
				if L[i]<=L[j]:
					temp+=1
					i=j
					j+=1
				else:
					i=j
					j=0
			else:
				i=j
				j=0
		if temp>result:
			result=temp
			temp=1
	
	if temp>result:
		result=temp

	return result	

print longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2])
print longestRun([0]) 
print longestRun([1, 1, 1, 1, 1])
print longestRun([-10, -5, 0, 5, 10])
