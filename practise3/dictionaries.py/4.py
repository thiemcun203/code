n=int(input())
list_name=[]
while True:
    try:
        list_name.append(input().split())
    except:
        break
dic_name={}
for i in list_name:
    dic_name[i[0]]=i[1]
list_tree=[]
for i in dic_name.values():
    if i not in dic_name.keys():
        a=i
list_tree.append([a,0])
print(list_tree)
        
    
