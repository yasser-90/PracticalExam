from op import opriation as opar
n=int(input('input the range'))
x=int(input('input number'))
s=0
s2=0
power1=0
fac1=0
i=1
for i in range(n):
    power1=opar.power(x,i)
    fac1=opar.fac(i)
    s2=(fac1/power1)
    if  s2==0:
        print ("ZeroDivisionError: division by zero ")
        break
    else:
        s=s+s2
print(s)


