n=int(input())
s=[]
def tryl(k): #set start 
    global s
    for i in range(2): # loop all possible value of variable at k
    #if check.. -> check possible value is right 
        s.append(str(i)) # 'track' the value of varibale at k
        
        if k==n: # if k==n then do the request then 'back' to new value of variable at k+1
            print("".join(s))
            
        else:
            tryl(k+1) # mostly check k+1,....
        s.pop() # remove element gradually from n to offset to original -> back
    # ( if wrong -> back)
tryl(1)
