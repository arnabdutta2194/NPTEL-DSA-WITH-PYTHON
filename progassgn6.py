def transpose(m):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return rez
m=[[1,2,3],[4,5,6]]
print(transpose(m))


'''




def transpose(m):

    x=len(m)
    y=len(m[0])

    for i in range(x):
        for j in range(y):

                temp=m[i][j]
                m[i][j]=m[j][i]
                m[j][i]=temp
    return(m)


m=[[1,2,3],[4,5,6]]
print(transpose(m))
'''




