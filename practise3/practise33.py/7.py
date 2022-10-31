def sort_students(n):
    a=[list(i) for i in n]
    b=[[float(i[1]),i[0]] for i in a]
    b.sort(reverse=True)
    print(b)
    b=[[i[1],i[0]] for i in b]
    c=[tuple(i) for i in b]
    return c
tup = [('z', '6'), ('tem2', '12.20'), ('item3', '6')]
print(sort_students(tup))