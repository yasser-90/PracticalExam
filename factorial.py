def factorial(x):

    if x == 1:
        return 1
    else:
       
        return (x * factorial(x-1))

num = 7
result = factorial(num)
print("The factorial of", num, "is", result)

def power(y):
      n=input("enter the number:")
      if y == 0 :
            print("invalid number")
      else:
            for i in range(1,2,len(n)):
                  y=y*y
                  