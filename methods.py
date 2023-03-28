def fcatorial(n):
    fact = 1
    while n != 0:
        fact *= n
        n -= 1
    return fact


def power(number, n):
    return number**n


n = int(input('n='))
x = int(input('x='))

for i in range(1, n, 2):
    result = 0
    signle = 1
    resultFact = fcatorial(i)
    resultPower = power(x, i)
    result = (result*signle) + (fcatorial(i)/power(x, i))
    signle *= -1
