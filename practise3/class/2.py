class Rect():
    # def __init__(self,a, b):
    #     self.a=a
    #     self.b=b
    def __str__(self,a,b):
        return f"<Width = {a}, Height = {b}>"
        # return "<Width = "+str(self.a)+ ", Height = " +str(self.b)+ ">"
    def area(self,a,b):
        return int(a)*int(b)
    def perimeter(self):
        return 2*(self.a+self.b)
# thiem=Rect(4, 5)
print(Rect().__str__(4, 5))
print(Rect().area(4, 5))
# print(Rect().perimeter(4, 5))    error