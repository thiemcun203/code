n=int(input())
x=[0 for i in range(n)]
mark=[0 for i in range(n)]
def solution():
    for i in x:
        print(i, end=" ")
    print("")

def tryl(k):
    for i in range(1,n+1):
        if mark[i-1]==0:
            mark[i-1]=1
            x[k-1]=i
            
            if k==n:
                solution()
                
            else:   
                tryl(k+1)
            mark[i-1]=0 # k==n then mark at n =0 then mark n-1 = 0 then.... then i+1 ....
        
tryl(1)
        