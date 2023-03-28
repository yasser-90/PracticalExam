class function :
    def fact(n):
        temp = 1
        for c in range(n):
            temp = temp * ( c + 1 )
        return temp
    
    
    def power(x,n) :
        return x**n