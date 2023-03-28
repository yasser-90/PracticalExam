from new import fact,po 
n = int(input('n='))
x = int(input('x='))
sum = 1

for i in range(n):
    ser = (fact(n)/po(x, n))*sum  
    print(ser)
    # print(sum)
    sum = sum *(-1)  
    

