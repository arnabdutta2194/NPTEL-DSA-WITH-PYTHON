#Which of the following is correct?

 #x[1] == 40, y[1] == 40, w[0] == 50, u[0] == 50
 #x[1] == 4, y[1] == 40, w[0] == 4, u[0] == 50
 #x[1] == 50, y[1] == 50, w[0] == 50, u[0] == 50
 #x[1] == 40, y[1] == 40, w[0] == 4, u[0] == 50


x = [13,4,17,1000]
w = x[1:]
u = x[1:]
y = x
u[0] = 50
y[1] = 40
print(y)
print(x)
print(w)
print(u)

# ANS Option d