def valley(l):
  if(len(l)==0):
    return(True)
  if(len(l)==1):
    return(False)
  if(l[0]<l[1]):
    return(False)
  for i in range(0,len(l)-1):
    if(l[i]<l[i+1]):
      pos=i
      break
    if(l[i]==l[i+1]):
      return(False)
  else:
    return(False)
  for i in range(pos,len(l)-1):
    if(l[i]>=l[i+1]):
      return(False)
  return(True)


list=[3,2,1,2]
print(valley(list))