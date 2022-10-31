# # Python code to illustrate splitlines()
# string = "Welcome everyone to\rthe world of Geeks\nGeeksforGeeks"

# # No parameters has been passed
# print (string.split( ))

# # A specified number is passed
# print (string.splitlines())
# print('andnd\rsnnxxndx\nsss') # carry which after \r come at beginning
# # True has been passed
# print (string.zfill(2))
# lst=[7,9,7,6,4]
# print(lst[:3])
nums = [0, 4, 7, 2, 1, 0 , 9 , 3, 5, 6, 8, 0, 3] 

nums = filter(lambda x: x%5==0, nums)
print(i for i in nums)
for i in nums:
    print(i)
# def di(x):
#     return x%5
# nums = map(di, nums)
# print(list(nums))
f = open('workfile', 'wb+')
f.write(b'0123456789abcdef')
print(f.seek(5,1))
def foo():
    try:
        return 1
    finally:
        return 3
k = foo()
print(k)
int('65')
Print(“Good Morning”)
print(“Good night)