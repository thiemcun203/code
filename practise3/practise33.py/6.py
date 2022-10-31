temp = input().split(' ')
m, n = int(temp[0]), int(temp[1])
a = []
b = []
for i in range(m):
  a.append(input().split(' '))
for i in range(m):
  b.append(input().split(' '))
sum = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        sum[i][j] = int(a[i][j])+int(b[i][j])
for i in range(m):
    print(*sum[i])
