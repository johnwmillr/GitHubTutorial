def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

class Fraction(object):

    def __init__(self, num, den):
        self.num = int(num / gcd(abs(num), abs(den)))
        self.den = int(den / gcd(abs(num), abs(den)))

    def __str__(self):
        return "{0}/{1}".format(self.num, self.den)

    def __add__(self,f2):
        return Fraction(self.num*f2.den+f2.num*self.den,self.den*f2.den)

    # TODO: Implement subtraction
    # def __sub__(self,f2):
        # return ...

    # TODO: Implement multiplication
    # def __mul__(self,f2):
        # return ...

    # TODO: Implement divition
    # def __div__(self,f2):
        # return ...

    def __repr__(self):
        if self.num==self.den:
            return "1"
        else:
            return str(self.num) + "/" + str(self.den)        

    def __float__(self):
        return self.num/self.den

    @property
    def eval(self):
        return self.__float__()
