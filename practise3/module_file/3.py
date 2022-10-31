import numpy as np
def system_solver(a):
    (m,n)=np.shape(a)
    A=a[:,:-1]
    B=a[:,-1]
    # print(np.dot(B))
    return np.linalg.inv(A).dot(B)
a = np.array([[1, 3, -2, 5], 
	        [3, 5, 6, 7], 
	    [2, 4, 3, 8]])
print(system_solver(a))
