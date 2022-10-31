# # import math
# # class Figure:
# #     def __init__(self, a, b=0, c=0):
# #         self.a=a
# #         self.b=b
# #         self.c=c
        
# #     def perimeter(self):
# #         if self.c==0:
# #             return 2*(self.a+self.b)
# #         # if self.b==self.c==0:
# #         #     return self.a*2*math.pi
# #         return self.a +self.b+self.c
    
# #     def area(self):
# #         if self.c==0:
# #             return self.a*self.b
# #         # elif self.b==0 and self.c==0:
# #         #     return math.pi*(self.a**2)
# #         else:
# #             p=(self.a+self.b+self.c)/2
# #             return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
# # import numpy as np
# # X, y = np.arange(10).reshape(2,5,order="c"), range(5)
# # print(X[:,[1,3]])
# # if 4:
# #     print(2)
# def solution(a):
#     if -1 not in a:
#         return sorted(a)
#     elif all(a):
#         return a
#     else:
#         lst=[]
#         ls=[]
#         for i in range(len(a)):
#             if a[i]==-1:
#                 lst.append(i)
#             else:
#                 ls.append(a[i])
#         ls.sort()
#         for i in lst:
#             ls.insert(i,-1)
#         return ls  
# a= [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
# print(solution(a))

# lst=[]
# ls=[]
# for i in range(len(a)):
#     if a[i]==-1:
#         lst.append(i)
#     else:
#         ls.append(a[i])
# ls.sort()
# for i in lst:
#     ls.insert(i,-1)
# print(ls)
from email.mime import image
from unittest import result


x="hello"
# assert x=="helo", "dung"
# assert x=="dung", "dddd"

# def solution(inputArray):
#     ia=inputArray
#     len=2
#     i=1
#     while i*len<=max(ia):
#         if i*len in ia:
#             len+=1
#             i=0
#             print("day la len",len)
#         i+=1
#         print("day la i",i)
#     return len
# print(solution([5, 3, 6, 7, 9]))
# def solution(image):
#     im=image
#     n=len(image)
#     result=[[(im[i-1][j-1]+im[i-1][j]+im[i-1][j+1] \
#             + im[i][j-1]+im[i][j]+im[i][j+1] \
#             + im[i+1][j-1]+im[i+1][j]+im[i+1][j+1])//9 for j in range(1,n)] for i in range(1,n)]
#     return result
image=[[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
matrix=[[True,False,False], 
 [False,True,False], 
 [False,False,False]]
# print(solution(image))
# print(image[0:3][:3])
matrix=[[False]*len(matrix[0])]+ matrix + [[False]*len(matrix[0])]
for i in range(len(matrix)):
    matrix[i]= [False]+ matrix[i] + [False]
result=[]
for i in range(1,len(matrix)-1):
    re=[]
    for j in range(1,len(matrix[0])-1):
        lst = [matrix[i+k][j-1:j+2] for k in [-1,0,1]]
        s=0
        for m in range(3):
            s+=lst[m].count(True)
        if matrix[i][j]:
            re.append(s-1)
        else: re.append(s)
    result.append(re)
print(-2*False)
        
    



    
        
        
            

