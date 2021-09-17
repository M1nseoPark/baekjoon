import sys

n = int(sys.stdin.readline())
A = []
for i in range(n):
    B = list(sys.stdin.readline().split())
    A.append(B)

A.sort(reverse=True)
A.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))   // 앞에 - 붙여주면 내림차순 정렬
for i in range(n):
    print(A[i][0])
