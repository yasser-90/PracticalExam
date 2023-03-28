class operations:
    def __init__(self,fact,pow):
        self.fact=fact
        self.pow=pow

    def facatorial():
        x=input(int('input number :'))
        i=1
        while i < x:
            F=x*i
            x=x+1
            print('this is factorial for this', F)
            print(F)
            continue
        if x == i:
            print(x)
        return F

    def power():
        x=input(int('input number :'))
        pow=x*x
        print(pow)
        return pow

    num=input(int('input number :'))
    if num % 3 == 0 :
        x=num
        n=range(1,100,3)
    S = (F*1/x^1)-(F*3/x^3)+(F*1/x^5)+(F*n/x^n)   #s=!1/x^1 - !3/x^3 + !5/x^5 ........... !n/x^n
    print(S)

F1=operations()
F1=facatorial()
P1=power()



