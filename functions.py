import math


#n=input('n=')

class function():

    def fact(fac):
    
        res = math.factorial(fac)
        return res


    def pow(po,p):
        res = math.pow(po,p)
        return res

print(function.pow(2,2))
print(function.fact(5))