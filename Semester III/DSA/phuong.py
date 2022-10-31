n=int(input())
def add(x):
    x=list(x)
    k=n-1
    while k>0 and x[k]=='1':
        x[k]='0'
        k-=1
    x[k]='1'
    return "".join(x)
start="0"*n
for i in range(2**n):
    print(start)
    start=add(start)
    
 




