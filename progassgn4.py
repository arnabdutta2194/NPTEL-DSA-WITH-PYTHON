def descending(l):
    N=len(l)
    if (N== 0 or N == 1):
        return True

    for i in range(1,N-1):
        if(l[i-1]>=l[i]):

            c=True
        else:
            c= False
    return c
l=[4,1,2,1]
print(descending(l))