from list_utilities import *
nested_lst=eval(input())
print(*flatten_nested_list(nested_lst))
print(max_num_in_list(flatten_nested_list(nested_lst)))
# str=""
# for i,u in enumerate(nested_list):
#     if u.isdigit()==True:
#         if nested_list[i+1].isdigit()==False:
#             str+=u
#             str+=" "
#         else:
#             str+=u
# file=str.strip().split(' ')
# fileint=[int(i) for i in file]
# print(*file)
