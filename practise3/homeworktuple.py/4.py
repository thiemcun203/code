def closest_tuple(tuple_list, query, k) :
    closest=tuple_list[0]
    for i, u in enumerate(tuple_list):
        if i==0: continue
        if abs(tuple_list[i-1][k-1]-query[k-1]) <= abs(tuple_list[i][k-1]-query[k-1]):
            closest=tuple_list[i-1]
    return closest

    