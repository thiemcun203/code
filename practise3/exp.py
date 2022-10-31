p=123
def exp(x,n):
    if n==1:
        return x%p
    else:
        A=exp(x,n//2)
        if n%2==0:
            return A*A%p
        else:
            return A*A*x%p
print(exp(4,10))
# {[ (res*x) mod p] * x } mod p