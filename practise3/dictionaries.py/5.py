def L(arr,i,d):
    if i in d:
        return d[i]
    else:
        res=1
        for k in range(0,i):
            if int(arr[i])*int(arr[k])<0 and abs(int(arr[i]))>abs(int(arr[k])):
                res= max(res,1+L(arr,k,d))
        d[i]=res
        return res
def ans(arr):
    ans=0
    d={0:1}
    for i in range(len(arr)):
        ans=max(ans,L(arr,i,d))
    return ans
if __name__=="__main__":
    n=int(input())
    arr=[ int(i) for i in input().split()]
    print(ans(arr))

