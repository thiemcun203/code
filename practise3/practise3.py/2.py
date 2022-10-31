def check(n):
    if n<=1: return 0
    if n==2:return 1
    else:
        a=1
        for i in range(2,int(n**0.5)+1):
            if n%i==0: a=0
    return 1 if a==1 else 0

def check_sum(n):
    if check(n)==1 and check(n-2)==1: 
        print(2)
        print(n-2)
    else:
        print(0)
print(check(5))
print(check(4))
check_sum(19)
check_sum(20)