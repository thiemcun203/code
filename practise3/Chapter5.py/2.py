n=int(input())
arr=list(map(int,input().split()))
x=int(input())
brr=list(map(lambda y: abs(y-x), arr))
brr.sort()
for i in arr:
    if abs(i-x)==brr[0]:
        print(i)
        break



