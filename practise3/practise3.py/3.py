import math
def check(m):
    file=[int(input()) for i in range(m)]
    sum=0
    for i in file:
        if i<0: fx= math.cos(4.5*(i**2)) +5*math.sin(i**3-1)
        elif i==0: fx=7
        else: fx= math.log2(i)+(i**2+5)**0.5
        sum+=fx
    print(sum)
check(4)
