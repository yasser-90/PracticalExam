

def fac(x):

    if x == 1:
        return 1

    else:
        return x *fac(x-1)

def poww(x,s):
    return x**s
n = int(input('n='))

g= 1
sum = 0
for i in range(1,n+1,2):
    sum = sum + (fac(i)/poww(i,i))*g
    g=g*-1

print(sum)