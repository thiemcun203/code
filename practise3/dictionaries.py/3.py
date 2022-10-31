text=[]
while True:
    try:
        text.append(input())
    except:
        break
list_keys=[]
for i in text:
    list_keys+=i.split()
s=[]
thiem={}
for i in list_keys:
    if i not in thiem:
        thiem[i]=0
        s.append(thiem[i])
        
    else:
        thiem[i]+=1
        s.append(thiem[i])
print(*s)
        
        
    
    
    