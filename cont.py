class con:

    def fac(self,x):

        if x == 1:
            return 1

        else:
            return x * self.fac(x - 1)

    def poww(self,x, s):
        return x ** s