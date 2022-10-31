from time import time


import time


n=int(input())
text=[]
for i in range(8):
    text.append(input().split())
t1=time.time()
# dic_name={}
# for i in list_name:
#     dic_name[i[0]]=i[1]

# dic_tree={}
# #find ancestor
# for i in dic_name.values():
#     if i not in dic_name:
#         ancestor = i
# dic_tree[ancestor]=0
# #find height of line
# def height(i):
#     if dic_name[i] == ancestor:
#         dic_tree[i]=1
#         return dic_tree[i]
#     else:
#         dic_tree[i] = height(dic_name.get(i,ancestor))+1
#         return dic_tree[i]
#call all function to make full dictionary
# for i in dic_name:
#     height(i)
# for i in sorted(dic_tree.items()):
#      print(i[0],i[1])
dic={}

for ele in text:
    dic.update({ele[0]:ele[1]})

for key,value in dic.items():
    if value not in dic.keys():
        ancestor=value
dic2={ancestor:0}

def family_tree(n,dic2):
    if n in dic2:
        return dic2[n]
    else:
        dic2[n]= 1+family_tree(dic[n],dic2)
        return dic2[n]

for i in text:
    family_tree(i[0],dic2)
res=dict(sorted(dic2.items(),key=lambda x:x[0]))

for key,value in res.items():
    print(key,value)

t2=time.time()
print(t2-t1)

