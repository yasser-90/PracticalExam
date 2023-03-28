import math 
def fact(n):
    for i in range(1,n+1,2):
        # print(i)
        k = math.factorial(i) 
        print(k)
    

def po(x,n):
    for i in range(1,n+1,2):
        y = math.pow(x, i)
        print(y)
        



n = int(input('n='))
x = int(input('x='))
# s = fact(n) / po(x,n)
x = -1
for i in range(n):
    ser = fact(n)  +  po(x,n) * x
    print(ser)
    print(x)
    x = x *(-1)  
    


