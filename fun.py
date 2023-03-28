class operation:
    def factorial(x): 
        if x < 0:    
                        print(" Factorial does not exist for negative numbers")    
  
        elif x == 0:   
                        print("The factorial of 0 is 1")    
        else: 
                        for i in range(1,x + 1):    
                                        x = x*i   
        return x  
        
 


def power(x,y):
        for i in range(1,y):
                x=x*x
        return x


#n=input('n=')
#s=factorial(n)/pow(x,n) - factorial(n)/pow(x,n) + factorial(5)/pow(x,n)        


        

