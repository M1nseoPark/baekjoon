# 행렬 A 입력
n, m = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

# 행렬 B 입력
m, k = map(int, input().split())
B = []
for i in range(m):
    B.append(list(map(int, input().split())))

# A x B 계산
AB = [[0] * k for _ in range(n)]   # A x B의 크기는 n x k
for i in range(n):
    for j in range(k):
        for t in range(m):
            AB[i][j] += A[i][t] * B[t][j]

for i in AB:
    for j in i:
        print(j, end=' ')
    print()
