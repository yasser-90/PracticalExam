n=input('n=')


def factorial(n, fact = 1):
    if n:
        return factorial(n-1, fact*n)
    else:
        return fact


def power(b, n):
    b2 = 1
    for i in range(n):
        b2=b2*b 
    return b2

s = 0
sign = 1
x = 2
for i in range(1,int(n)+1,2):
    s+= sign*(factorial(i)/power(x, i))
    # print(sign*(factorial(i)/power(x, i)))
    sign*=-1
    print(i)


print(s)