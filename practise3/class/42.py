import math
class FuncWithDerivatives(object):
    def __init__(self, h=1.0E-5):
        self.h = h  # spacing for numerical derivatives
    def __call__(self, x):
        raise NotImplementedError('__call__ missing in class %s' % self.__class__.__name__) #-> annouce have to declare __call__ in class
        # return math.sin(x)
    def df(self, x):
        """Return the 1st derivative of self.f."""
        # Compute first derivative by a finite difference
        h = self.h
        return (self(x+h/2) - self(x-h/2))/(h)
    def ddf(self, x):
        """Return the 2nd derivative of self.f."""
        # Compute second derivative by a finite difference:
        h = self.h
        return (self(x+h) - 2*self(x) + self(x-h))/(float(h)**2)
class Sine1(FuncWithDerivatives):
    def __call__(self, x):
        return math.sin(x)
class Sine2:
    def __call__(self, x):
        return math.sin(x)
    def df(self,x):
        return math.cos(x)
    def ddf(self,x):
        return -math.sin(x)
s1 = Sine1()
s2 = Sine2()
x = math.pi /3
print("%.5f %.5f" % (s1(x), s2(x)))
print("%.5f %.5f %.5f %.5f" % (s1.df(x), s2.df(x), s1.ddf(x), s2.ddf(x)))