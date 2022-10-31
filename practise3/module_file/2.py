import numpy as np
def convert(arr):
#     (r,c)=np.shape(arr)
#     return np.array([[i/sum(np.array(arr[k])) for i in arr[k]] for k in range(r)])
    a=arr.astype(np.float)
    b=sum(a, axis=1, keepdim=True)
    return a/b
