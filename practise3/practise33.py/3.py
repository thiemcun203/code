s=input()
import re
a=re.sub("\s\s+"," ",s)
a=a.strip()
print(a)
