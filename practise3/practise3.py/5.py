import cmath
a=float(input())
b=float(input())
c=float(input())
delta=b**2-4*a*c
if a==0 and b==0 and c!=0: print("No roots")
elif a==0: print(-c/b)
else:  
    print((-b+cmath.sqrt(delta))/(2*a))
    print((-b-cmath.sqrt(delta))/(2*a))
