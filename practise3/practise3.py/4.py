import math
a=[[float(input()) for i in range(2)]]
b=[[int(-2+i*0.5),int(5-i*1)] for i in range(17)]
c=a+b
for i in range(len(c)):
    x,y=c[i][0],c[i][1]
    if x<y-2:print( 3*(x**2)-math.log(y))
    elif y-2<=x<=y+2: print((x+y)/2+8)
    else: print(y**3+2*math.sin(x))

        

    