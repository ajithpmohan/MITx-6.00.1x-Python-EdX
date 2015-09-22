s = 'bbobbwiboobobobcbobblbobbbobobboobo'
count = 0
for elem in range(len(s)-2):
  if s[elem]+s[elem+1]+s[elem+2]=='bob':
    count+=1
print 'Number of times bob occurs is: '+ str(count)