n, m = map(int, input().split())
A = list(map(int, input().split()))
ret = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            total = A[i] + A[j] + A[k]
            if ret < total and total <= m:
                ret = total

print(ret)
