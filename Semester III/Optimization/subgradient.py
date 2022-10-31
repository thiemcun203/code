import numpy as np
x=np.array([0,0])
a=np.array([1,1])
f=[2*x[0]-3*x[1]+4, 5*x[0]+x[1]-3 , -3*x[0]+x[1]+2]
df=np.array([[2,-3],[5,1],[-3,1]])
def fx(x):
    max=f[0]
    for i in range(len(f)):
        if max <= f[i]:
            max=f[i]
            g=np.array(df[i])
    return g
while True:
    g=fx(x)
    x=x-a.dot(g)
    if a.dot(g) <=0.001:
        break
print(x)
