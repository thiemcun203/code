class Fraction():
    def __init__(self,num,deno):
        self.num=num
        self.deno=deno
    def __str__(self):
        return str(self.num)+"/"+str(self.deno)
    def __add__(self, other):
        res_num=self.num*other.deno+self.deno*other.num
        res_deno=self.deno*other.deno
        return Fraction(res_num,res_deno)
    def __sub__(self,other ):
        res_num=self.num*other.deno-self.deno*other.num
        res_deno=self.deno*other.deno
        return Fraction(res_num,res_deno)
    def inverse(self):
        return Fraction(self.deno,self.num)
    def __float__(self):
        return float(self.num/self.deno)
# if __name__=="__main__" : 
#     f1 = Fraction(3, 5)
#     f2 = Fraction(6, 7)
#     print(f1)
#     print(f1 + f2)
    