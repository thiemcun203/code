text = []
while True:
    try:
        text.append(input())
    except:
        break
thiem=dict()
for i in text:
    for u in i.split():
        if u not in thiem:
            thiem[str(u)]=1
        else:
            thiem[str(u)]+=1
max_value=int(max(thiem.values()))
min_value=int(min(thiem.values()))
list_final=[]
for i in range(max_value,min_value -1, -1):
    list_value= [k for k,u in thiem.items() if u==i]
    for i in list_value:
        list_value.sort()
    list_final+=list_value
for i in list_final:
    print(i)
    


