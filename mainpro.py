from functions import factorial, power

n=int(input('n='))
x=int(input('x='))

s = 0
sign = 1
for i in range(1,int(n)+1,2):
    s+= sign*(factorial(i)/power(x, i))
    sign*=-1


print('Ther result is : ', s)