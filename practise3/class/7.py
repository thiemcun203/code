class Matrix():
    def __init__(self, matrix):
        self.matrix=matrix
    def __str__(self):
        s=[ "\t".join(str(k) for k in i) for i in self.matrix ]
        return str("\n".join(s))
        
    def size(self):
        ma=self.matrix
        return (len(ma),len(ma[0]))
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m.size())