a=[[i for i in range(1,1001) if i%j==0] for j in range(2,10) ]
b=[x for x in range(1,1001) if 0 in [x%i for i in range(2,10)]]
print(b)

