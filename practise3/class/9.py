import time
t1=time.time()
class Matrix:
    def __init__(self, M):
        self.M=M
        
    def solve(self, b):
        import numpy as np
        A=np.array(self.M)
        B=np.array(b)
        C=[f'{i:.2f}' for i in np.linalg.solve(A,B)]
        return ' '.join(C)

m = Matrix([[1, 1, 1], [0, 2, 0], [0, 0, 4]])
print(m.solve([1,1,1]))
t2=time.time()
print(t2-t1)