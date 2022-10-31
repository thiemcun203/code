import math
class Figure:
    def __init__(self, a, b=0, c=0):
        self.a=a
        self.b=b
        self.c=c
        
    def perimeter(self):
        if self.c==0:
            return 2*(self.a+self.b)
        # if self.b==self.c==0:
        #     return self.a*2*math.pi
        return self.a +self.b+self.c
    
    def area(self):
        if self.c==0:
            return self.a*self.b
        # elif self.b==0 and self.c==0:
        #     return math.pi*(self.a**2)
        else:
            p=(self.a+self.b+self.c)/2
            return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
class LengthException(Exception):
    
    pass
class InvalidTriangleException(Exception):
    pass
class Rectangle(Figure):
    def __init__(self, a, b):
        Figure.__init__(self,a, b)
        if a<0 or b<0: print(str(type(LengthException())) + ' was raised')
class Circle(Figure):
    def __init__(self, a):
        Figure.__init__(self, a)
        if self.a<0: print(str(type(LengthException())) + ' was raised')
    def area(self):
        return math.pi*(self.a**2)
    def perimeter(self):
        return self.a*2*math.pi
class Triangle(Figure):
    def __init__(self, a, b, c):
        if a<0 or b<0  or c<0 : print(str(type(LengthException())) + ' was raised')
        lst=sorted([a,b,c])
        if not (lst[0]>lst[2]-lst[1] or lst[2]<lst[0]+lst[1]): print(str(type(InvalidTriangleException())) + ' was raised')
        Figure.__init__(self,a,b,c)
a=Rectangle(2,3)
print(a)
