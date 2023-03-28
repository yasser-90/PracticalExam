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
