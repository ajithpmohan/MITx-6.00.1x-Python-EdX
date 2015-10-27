def getSublists(L,n):
	results=list()
	temp=list()
	i=0
	count=0
	while(i < len(L)):
		count+=1
		if count<=n:
			temp.append(L[i])
			i+=1
		else:
			results.append(temp)
			temp=list()
			count=0
			i=i+1-n
	if temp:
		results.append(temp)
	return results



print getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2],4)
#The Output shoould be [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]

print getSublists([1, 1, 1, 1, 4],2)
#The Output shoould be [[1, 1], [1, 1], [1, 1], [1, 4]]