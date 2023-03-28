# s =!1/x ^ 1 - !3/x ^ 3 + !5/x ^ 5 ................. !n/x ^ n


def fcatorial(number):
    fact = 1
    number += 1
    for i in range(1, number):
        fact *= i
    return fact


def power(number, power):
    return pow(number, power)
