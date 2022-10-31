import pickle
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
with open('lists.pkl','wb') as f:
    pickle.dump(a,f)
    pickle.dump(b,f) 

with open('lists.pkl', 'rb') as f:
    c= pickle.load(f)
    d=pickle.load(f)
f.close()
result = [i + j for i, j in zip(c, d)]
print(result)