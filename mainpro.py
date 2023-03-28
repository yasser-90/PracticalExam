from cont import con
co = con()


n = int(input('n='))

g= 1
sum = 0
for i in range(1,n+1,2):
    sum = sum + (co.fac(i)/co.poww(i,i))*g
    g=g*-1

print(sum)



