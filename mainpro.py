from function import *

n=int(input('n= '))
x=int(input('x= '))

sum = 0
sign = 1

for i in range(1,n+1,2):
    sum += ( factorial(i) / power(x,i) ) * sign
    sign *= -1

print(sum)
