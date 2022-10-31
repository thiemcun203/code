n=int(input())
lst=[ int(i) for i in input().split()]
s=[0 for i in range(n)]
s[0]=lst[0]
res=s[0]
for i in range(1,n):
    if s[i-1]>0:
        s[i]=s[i-1]+lst[i]
    else:
        s[i]=lst[i]
    if res < s[i]:
        res=s[i]
print(res)
    
    