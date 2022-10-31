tmp = input().split(' ')
m, n = int(tmp[0]), int(tmp[1])
i=1
def a(n):
    n=0
    i+=1
    return i
matrix=[[i+1+j*n for i in range(n) ] for j in range(m)]
for i in matrix:
    print( *i )