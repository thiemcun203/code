n,M=[int(i) for i in input().split() ]

s=[0 for i in range(n+1)]

def check(v,k): 
    if k<n: return T+v<M
    else: return T+v==M 
    
    
def solution():
    for i in s[1:]:
        print(i,end=" ")
    print("")
T=0
def tryl(k):
    global T
    
    for v in range(1,M-T-(n-k)+1): 
        # choose one
        
        if check(v,k): # check
            s[k]=v #track
            T+=v
            if k==n:
                solution()
                
            else:
                tryl(k+1)
                
            T-=v # back if reach final or reach error at next position
        
        #choose others

tryl(1)
#choose one -> check -> track -> if k==n-> back or k!=n try k+1 ->back 
#            not satisfied -> choose another