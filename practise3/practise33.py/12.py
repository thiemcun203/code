def merge_dict(d1, d2):
    for i in d2:
        if i in d1:
            d1[i]=d1[i]+d2[i]
        else:
            d1[i]=d2[i] 
    return d1
