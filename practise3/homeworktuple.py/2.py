def sum_and_count(n):
    sm=[sum(i) if type(i) is not int else i for i in list(n) ]
    count=[len(i)  if type(i) is not int else 1 for i in list(n)]
    return sm, count
inp = ((1,2,5), (3,7,5,10), (1))
sum_list, cnt_list = sum_and_count(inp)
print(*sum_list)
print(*cnt_list)