import numpy as np
x=np.array([0,0,0])
f=x[0]*x[0] + x[1]*x[1] + x[2]*x[2] - x[1]*x[2] - x[2]*x[2] + x[1] + x[2]

f2= np.array([
    [2, -1, 0],
    [-1,2,-1],
    [0,-1,2]
])
f2_inverse=np.linalg.inv(f2)
def f1(x1,x2,x3):
    return np.array([2*x1-x2+1,2*x2-x1-x3, 2*x3-x2+1])
k=0
y=x
while np.sum(np.abs(y-x)) <= 0.0003 :
    if np.linalg.norm(f2_inverse.dot(f1(x[0],x[1],x[2])))==0:
        break
    y=x
    x=x-f2_inverse.dot(f1(x[0],x[1],x[2]))
    
print(f2_inverse)
print(f1(x[0],x[1],x[2]))
print(x)
    







