def C(k: int, n: int):
    if k == 0 or k == n:
        return 1
    factorial = [1]
    for i in range(0, n):
        factorial.append( (i + 1) * factorial[i])
    return factorial[n] // factorial[n - k] // factorial[k]
k, n = [int(value) for value in input().split()]
print(C(k,n)%1000000007)