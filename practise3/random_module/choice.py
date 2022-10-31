import random
import time
list_type_balls=["Green","Blue","Red"]
#weight: the number of each colour of ball
#k: the number of picking
t1=time.time()
results_after_kth=random.choices(list_type_balls, weights=[5,3,2], k=10000000)
print(int(results_after_kth.count('Blue'))/10000000)
t2=time.time()
print(t2-t1)