#from numpy import *
import numpy as np
arr = np.array([[[[i for i in range(5)] for j in range(4)] for k in range(3)] for n in range(2)])
print(arr.shape)

print(arr)
print(np.__version__)
# arr = np.array([1, 2, 3, 4], ndmin=2)
arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(arr)
print(arr[1, 0])
arr = np.array([10, 15, 20, 25, 30, 35, 40])

print(arr[1:5])
arr = np.array([10, 15, 20, 25, 30, 35, 40])

print(arr[1:5:2])
arr = np.array([10, 10, 2022],dtype="S")

print(*arr[::2])
print(arr.astype("i"))
# import numpy as np

arr = np.array('appleDD', dtype="S")

print(arr.dtype)

print(list(range(9)))
arr1 = np.array([[[1, 2], [3, 4],[23, 56]]])

arr2 = np.array([[[5, 6], [7, 8],[456,32]]])

arr = np.concatenate((arr1, arr2), axis=2) # concatenate axis =dimension=0 ngoai vao, tung cap
print(arr)