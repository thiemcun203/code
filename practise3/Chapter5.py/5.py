n=int(input())
Block=[[[int(x) for x in input().split()] for j in range(8)] for i in range(n)]
def minus(n):
    return n[0]-n[1]
def add(n):
    return n[0]+n[1]
for m in range(n):
    for t in range(8):
        [i,j]=Block[m][t]
        a=0
        for k in range(t+1,8):
            if Block[m][k][0]== i or Block[m][k][1]== j or minus(Block[m][k])==minus([i,j])  or add(Block[m][k])==add([i,j]):
                a=1
                break
        if a==1: break
    print("NO" if a==0 else "YES")       
                
        

    