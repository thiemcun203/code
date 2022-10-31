s=input()
s=list(s)
s=[ u for i,u in enumerate(s) if u.isalpha()==True or (u== " " and u!=s[i-1]) or i==0]
s="".join(s)
s=s.strip()
print(s)
