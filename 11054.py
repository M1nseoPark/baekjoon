n = int(input())
A = list(map(int, input().split()))

ur = [0 for i in range(n)]
dr = [0 for i in range(n)]
result = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if A[j] < A[i] and ur[i] < ur[j]:
            ur[i] = ur[j]
    ur[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if A[j] < A[i] and dr[i] < dr[j]:
            dr[i] = dr[j]
    dr[i] += 1

for i in range(n):
    result[i] = ur[i] + dr[i] - 1
    
print(max(result))
