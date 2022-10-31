k=int(input())
string=str(input()).lower()

#make a dict with changed position
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet1=alphabet.copy()
n=len(alphabet)
K=k%n
for i in range(n):
    if i < n-K:
        alphabet[i]= alphabet1[i+K-n]
    else:
        alphabet[i]=alphabet1[i+K-n]
thiem={alphabet1[i]:alphabet[i] for i in range(n)}

#transform
a=list(string)
for i in range(len(a)):
    if a[i].isalpha()==True:
        a[i]=thiem[a[i]]
b="".join(a)
print(b)

        
        

    
    