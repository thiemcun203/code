class Matrix:
    def __init__(self, matrix):
        self.matrix=matrix
    def __str__(self):
        s=[ "\t".join(str(k) for k in i) for i in self.matrix ]
        return str("\n".join(s))
    def __add__(self, other):
        sum=[[x+y for x,y in zip(a,b)] for a,b in zip(self.matrix, other.matrix)]
        return Matrix(sum)
    def __mul__(self, scalar):
        mul=[[scalar*int(i) for i in k] for k in self.matrix]
        return Matrix(mul)
    def __rmul__(self, scalar):
        # return Matrix.__mul__(self,scalar)
        return self.__mul__(scalar)
    def thiem(self):
        return 223
print(Matrix.thiem(Matrix().__init__([3,2])))
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
alpha = 15
print(m * alpha)
print(alpha * m)
print(Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).__mul__(10))
print(Matrix.__mul__(m1,10))
print(m1.__mul__(10))
        