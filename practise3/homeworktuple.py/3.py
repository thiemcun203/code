def tup2num(n):
    a=""
    for i in n:
        a+=str(i)
    return int(a)
tup = (1, 23, 567)
print(tup2num(tup))