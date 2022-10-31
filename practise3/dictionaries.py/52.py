n = input()
s = input().split(" ")
s = [int(x) for x in s]

a = [1]*len(s)

for i in range(1, len(s)):
    n = 0
    for j in range(i):
        if (s[j] * s[i] < 0) and (abs(s[j]) < abs(s[i])) and (a[j] > n):
            n = a[j]
            print(n)
    print("\n")      
    a[i] = n + 1
print(max(a))