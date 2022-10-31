import math
import trig
n=int(input())
Sumtrig=0
Summath=0
for i in range(1,21):
    if i%2!=0:
        Sumtrig+=trig.sin(n+i)
        Summath+=math.sin(n+i)
    else:
        Sumtrig+=trig.cos(n+i)
        Summath+=math.cos(n+i) 
print(f'Your own implementation:     {Sumtrig:.6f}')
print(f'Math module implementation:  {Summath:.6f}')
