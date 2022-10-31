text = []
while True:
    try:
        text.append(input())
    except:
        break
thiem=dict()
for i in text:
    a=i.split()
    if str(a[0]) not in thiem:
        thiem[str(a[0])]=int(a[1])
    else:
        thiem[str(a[0])]=int(thiem.get(a[0],0)) + int(a[1])
thiem1=thiem.items()
thiem2=sorted(thiem1)
for i in thiem2:
    i=list(i)
    print(*i)

    
        
        
        
    