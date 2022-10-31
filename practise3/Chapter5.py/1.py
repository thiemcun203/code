arr=list(map(int, input().split()))
brr=[]
for i, u in enumerate(arr):
    if i==0: continue
    if arr[i-1]<arr[i]:
        brr.append(arr[i])
if len(brr)==0:
    print("NONE")
else:
    print(*brr)  

