import copy
from functools import reduce

n=int(input())
inp_matrix=[[int(i) for i in input().split()] for j in range(n)]

x=[0 for i in range(n)]
mark=[False for i in range(n)]
f=0
# f_best=n*max(inp_matrix[0])
# for i in inp_matrix:
#     if max(i)>=f_best:
#         f_best=max(i)
f_best=100000000
def check(v):
    return not mark[v]
# lst=[]
lst=reduce(lambda x,y: x + y, inp_matrix)
lst = list(filter(lambda x: x!=0, lst))
# for i in range(n):
#     for j in range(n):
#         if inp_matrix[i][j]!=0:
#             lst.append(inp_matrix[i][j])

cm=min(lst)

def solution():
    global f_best
    if f+inp_matrix[x[-1]][x[0]] <= f_best:
        f_best=f+inp_matrix[x[-1]][x[0]]
        # y= copy.deepcopy(x)
    

    
def Try(k):
    global f
    for v in range(n):
        if check(v):
            mark[v]=True
            x[k]=v
            f+=inp_matrix[x[k-1]][x[k]]
            
            if k==n-1:
                solution()
                # print(x, f'{f+inp_matrix[x[-1]][x[0]]}')
            else:
                g= f + cm*(n-k)
                if g <= f_best:
                    Try(k+1)

            mark[v]=False
            f-=inp_matrix[x[k-1]][x[k]]
            x[k]=0
            
                
Try(0)
print(f_best)

#  
# ----
# 6
# 0 10 4 5 4 8
# 7 0 10 1 6 3
# 10 7 0 10 7 7
# 8 4 4 0 7 7
# 4 9 3 7 0 8
# 3 8 8 9 6 0
# ----
# 12
# 0 1 9 8 1 4 8 3 10 7 10 8
# 5 0 8 6 1 3 4 1 10 3 4 10
# 2 6 0 6 4 10 7 5 4 10 9 10
# 7 6 10 0 6 3 6 6 8 10 2 8
# 10 7 2 5 0 9 7 2 8 8 5 8
# 4 2 1 3 7 0 3 9 7 10 10 1
# 7 6 8 6 9 1 0 10 9 7 9 10
# 9 6 10 9 9 7 8 0 7 3 4 10
# 9 3 9 4 2 6 3 3 0 10 6 5
# 6 4 10 8 7 2 6 10 1 0 2 9
# 9 9 3 1 6 8 9 8 7 6 0 2
# 5 2 7 8 3 3 8 4 7 8 1 0
# ----
# 14
# 0 4 8 8 4 6 5 8 2 4 6 3 4 10
# 3 0 10 2 7 4 10 1 3 3 10 9 6 7
# 8 1 0 3 8 8 10 2 6 4 7 7 1 3
# 6 3 5 0 8 6 9 2 1 4 2 9 10 6
# 3 9 3 2 0 10 7 5 3 1 6 4 9 5
# 3 1 8 3 4 0 6 2 5 7 7 3 7 2
# 1 6 8 10 4 10 0 4 1 4 8 6 10 10
# 6 3 6 1 1 3 1 0 7 7 10 10 5 4
# 3 7 3 3 10 5 6 9 0 8 5 9 10 9
# 1 7 10 9 9 9 4 3 5 0 7 5 7 9
# 7 5 5 7 7 6 2 3 1 6 0 3 1 6
# 7 4 7 4 7 10 2 7 3 1 9 0 4 1
# 6 9 1 7 10 6 5 8 4 3 7 6 0 6
# 4 6 3 5 1 10 10 7 5 3 7 8 8 0
#  [0, 10, 4, 5, 4, 8],
#     [7, 0, 10, 1, 6, 3],
#     [10, 7, 0, 10, 7, 7],
#     [8, 4, 4, 0, 7, 7],
#     [4, 9, 3, 7, 0, 8],
#     [3, 8, 8, 9, 6, 0]
#     ]
