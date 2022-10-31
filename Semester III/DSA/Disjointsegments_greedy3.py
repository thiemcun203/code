n= int(input())
lst=[]
for i in range(n):
    lst.append([int(i) for i in input().split()])
lst.sort(key=lambda x: x[1])
count=1
x=lst[0]
for i in range(1,n):
    if lst[i][0]>x[1]:
        x=lst[i]
        count+=1
print(count)