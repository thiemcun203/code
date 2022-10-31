n=int(input())
s=[]
def check(v,k):
    if k==1:
        return True
    elif s[k-2]==str(v)=="1":
        return False
    return True

def tryl(k):
    for i in range(2):
        if check(i,k):
            s.append(str(i))
            if k==n:
                print("".join(s))
            else:
                tryl(k+1)
            s.pop()
tryl(1)
        
    