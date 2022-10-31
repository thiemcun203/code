def dictionary_convert(n):
    n=list(n)
    thiem=dict()
    for i in n:
        if i not in thiem:
            thiem[i]=1
        else:
            thiem[i]+=1
    return thiem
