from functions import factorial, power

n=input('n=')

s = 0
sign = 1
x = 2
for i in range(1,int(n)+1,2):
    s+= sign*(factorial(i)/power(x, i))
    sign*=-1


print('Ther result is : ', s)