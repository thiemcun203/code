#make a list without same elements, then remove elements in " duplicate" list
def remove_duplicates(lst):
    a=[]
    b=[]
    c=[]
    for i in lst:
        if i not in a:
            a.append(i)
        else:
            b.append(i)
    for i in b:
        if i in a:
            a.remove(i)
    return a
print(remove_duplicates([4, 3, 5, 2, 5, 1, 3, 5, 10, 3, 5, 2, 3 ]))