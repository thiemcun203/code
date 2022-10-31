p=10**9+7
def modOfexp(x,n):
    if n==1:
        return x%p
    else:
        A=modOfexp(x,n//2)
        if n%2==0:
            return A*A%p
        else:
            return A*A*x%p
x,n=[int(i) for i in input().split()]
print(modOfexp(x,n))