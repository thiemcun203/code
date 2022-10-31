import math
def sin(n):
    k=0
    f=1
    S=0
    while abs(f) >10**-9:
        f=((-1)**k)*(n**(2*k+1))/math.factorial(2*k+1)
        S+=f
        k+=1
    return S

def cos(n):
    k=0
    f=1
    S=0
    while abs(f) >10**-9:
        f=((-1)**k)*(n**(2*k))/math.factorial(2*k)
        S+=f
        k+=1
    return S
def exp(n):
    k=0
    S=0
    f=1
    while abs(f)>10**-9:
        f=n**k/math.factorial(k)
        S+=f
        k+=1
    return S
# print(sin(math.pi/2))