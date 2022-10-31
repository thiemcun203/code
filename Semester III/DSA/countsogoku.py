lst= [i.split()for i in [input() for i in range(9)]]
ltr=[[int(i) for i in lst[j]] for j in range(9)]
x=[[int(i) for i in lst[j]] for j in range(9)]

checkRow=[[False for v in range(10)] for r in range(9)]
checkColumn=[[False for v in range(10)] for c in range(9)] 
checkSquare=[[[False  for v in range(10)]for c in range(3)] for r in range(3)]

for r in range(9):
    for c in range(9):
        v=ltr[r][c]
        if v!=0:
            checkRow[r][v]=True
            checkColumn[c][v]=True
            checkSquare[r//3][c//3][v]=True

def check(v,r,c):
    return checkRow[r][v]==False and checkColumn[c][v]==False and checkSquare[r//3][c//3][v]==False

count=0
def solution():
    global count
    count+=1

def Try(r,c):
    if x[r][c]:
        if c==8 and r==8:
            solution()
        else:
            if c==8:
                Try(r+1,0)
                
            else:
                Try(r,c+1)
        return
    for v in range(1,10):
        if check(v,r,c):
             # tranh loi, co roi nhg k cong them
            x[r][c]=v
            checkColumn[c][v]=True
            checkRow[r][v]=True
            checkSquare[r//3][c//3][v]=True

            if c==8 and r==8:
                solution()
            else:
                if c==8:
                    Try(r+1,0)
                    
                else:
                    Try(r,c+1)
                    
            checkRow[r][v]=False
            checkColumn[c][v]=False
            checkSquare[r//3][c//3][v]=False
            x[r][c]=0
        
Try(0,0)
print(count)       
print(lst)






