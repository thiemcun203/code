n=int(input())
lst=[ int(i) for i in input().split()]
res=0
for i in range(n):
    weight=0
    
    for j in range(i,n):
        weight+=lst[j] #weight of each subsequence beginning at i
        if weight > res:
            res = weight
            
print(res)


    