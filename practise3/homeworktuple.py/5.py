list1=eval(input())
list2=eval(input())
same1=len(list1)-len(set(list1)-set(list2))
list3=[]
for i in list2:
    if i[0]!=i[1]:
        list3.append((i[1],i[0]))
same2=len(list1)-len(set(list1)-set(list3))
print(same1+same2)

    