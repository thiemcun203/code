N, K = map(int, input().split())
n=[[int(i) for i in input().split()] for j in range(K)]
Pins=["I"]*N
Pins_copy=Pins.copy()
for j in range(K):
    for i in range(n[j][0]-1,n[j][1]):
        Pins[i]="."
Pins="".join(Pins)
print(Pins)
