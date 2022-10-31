def step_tower(n,A,B,C):
    if n==1:
        print(f'{A}->{C}') 
    else: 
        step_tower(n-1,A,C,B)
        print(f'{A}->{C}')
        step_tower(n-1,B,A,C)
step_tower(5,"A","B","C")   