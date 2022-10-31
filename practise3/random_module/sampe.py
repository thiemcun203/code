import random
import time
list_balls=["blue","red","green"]
list_taking_kthballs=random.sample(list_balls, k=4, counts=[5,6,3])
#k=4: 2 blue 1 red 1 green
count=0
for i in range(1000000):
    list_taking_kthballs=random.sample(list_balls, k=4, counts=[5,6,3])
    if list_taking_kthballs.count("blue")==2 and list_taking_kthballs.count("red")==1 and list_taking_kthballs.count("green")==1:
        count+=1
print(count/1000000)
# print(count/10000)
#with for random is giving same value