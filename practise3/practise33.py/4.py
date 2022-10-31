s=input()
def mirror(s):
    thiem = {'b':'d','d':'b','i':'i','o':'o','q':'p','p':'q','v':'v','w':'w','x':'x'}
    a=""
    for i in s:
        if i in thiem:
            a+=thiem[i]
        else: return "NOT POSSIBLE"
    return a[::-1]



