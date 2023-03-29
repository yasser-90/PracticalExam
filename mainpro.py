n=input('n=')
def fact1():
    n = int (input ("Please enter a whole number: ") )
    fact = 1
    for factor in range (n,1,-1):
        fact = fact * factor
        
        print ("The factorial of", n, "is", fact)
        #main ()
def power(num):
    return num^num
print(power(num=))