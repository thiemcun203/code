def process(filepath):
    with open(filepath, 'r') as f:
        file=f.read()
        # print(" ".join(file.split())) use split() to adjust string
    file=file.split("\n")
    file=[i.split(' ') for i in file]
    dict={}
    for i in file:
        if i[0] not in dict:
            dict[i[0]]={i[1]:int(i[2])}
        else:
            if i[1] not in dict[i[0]]:
                dict[i[0]][i[1]]=int(i[2])
            else:
                dict[i[0]][i[1]]=int(i[2])+dict[i[0]][i[1]]
    for i in sorted(dict.keys()):
        print(f'{i}:')
        lst=sorted(list(dict[i].items()))
        for i in lst:
            print(*i)
    

filepath = '/Applications/Python 3.10/code/practise3/module_file/data1.inp'
process(filepath)
    