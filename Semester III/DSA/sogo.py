checkRow=[[False for v in range(10)] for r in range(9)] # ignore v=0, index from 0->8
checkColumn=[[False for v in range(10)] for c in range(9)] 
checkSquare=[[[False for v in range(10)] for c in range(3)] for r in range(3)] # -> then //3 to choose square
x=[[0 for c in range(9)] for r in range(9)]
def check(v,r,c):
    return checkRow[r][v]==False and checkColumn[c][v]==False and checkSquare[r//3][c//3][v]==False

def solution():
    for r in range(9):
        for c in range(9):
            print(x[r][c],end=" ")
        print("")
    print("-------------------------------")
def Try(r,c):
    for v in range(1,10):
        if check(v,r,c):
            x[r][c]=v
            checkRow[r][v]=True
            checkColumn[c][v]=True
            checkSquare[r//3][c//3][v]=True
            if c==8 and r==8 :
                solution()
            
            else:
                if c==8:
                    Try(r+1,0)
                else:
                    Try(r,c+1)
            checkRow[r][v]=False
            checkColumn[c][v]=False
            checkSquare[r//3][c//3][v]=False
Try(0,0)

    















