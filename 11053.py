n = int(input())
A = list(map(int, input().split()))

result = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))
