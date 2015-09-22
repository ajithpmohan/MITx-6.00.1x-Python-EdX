s = 'nnvlzdxyxrwryhenddivdn'
partial=s[0]
alpha=''
prev=s[0]
for i in range(1,len(s)):
  if s[i]>=prev:
    partial+=s[i]
  elif len(partial)>len(alpha):
    alpha=partial
    partial=s[i]
  else:
    partial=s[i]
  prev=s[i]
if len(partial)>len(alpha):
  alpha=partial
print 'Longest substring in alphabetical order is: '+ str(alpha)