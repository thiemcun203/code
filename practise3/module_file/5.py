#with open('/Applications/Python 3.10/code/practise3/module_file/test.inp') as f:
with open('/Applications/Python 3.10/code/practise3/module_file/data1.inp','r') as f:    
    file=f.read()
    file_copy=file
dict={}
k=0
for i, u in enumerate(file_copy):
    if u=='\n':
        n=i+k
        file=file[:n+1]+" "+file[n+1:]
        k+=1
      
file=file.split(" ")
for i in file:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

with open('test.out', 'w+') as f:
    f.write(str(dict))
with open('test.out', 'r') as f:
	all = f.read()
	print(all)
