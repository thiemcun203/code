n=int(input())
seq=[int(i) for i in input().split()]
def maxLeft(sub_seq,s,e):
    Max=-float("inf")
    Sum=0
    i=e
    while i >=s:
        Sum+=sub_seq[i]
        Max=max(Max,Sum)
        i-=1
    return Max
        
    
def maxRight(sub_seq,s,e):
    Max=-float("inf")
    Sum=0
    i=s
    while i <=e:
        Sum+=sub_seq[i]
        Max=max(Max,Sum)
        i+=1
    return Max
        

def maxSeq(seq,s,e):
    if s==e:
        return seq[s]
    else:
        m=(s+e)//2
        maxL=maxLeft(seq,s,m)
        maxR=maxRight(seq,m+1,e)
        return max(maxL+maxR, maxSeq(seq,s,m),maxSeq(seq,m+1,e))

print(maxSeq(seq,0,n-1))