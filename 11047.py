import sys

n, k = map(int, sys.stdin.readline().split())
A = []
for i in range(n):
    A.append(int(sys.stdin.readline()))

total = 0
pick = n - 1
ret = 0
while pick != -1:
    total += A[pick]
    if total > k:
        total -= A[pick]
        pick -= 1
    else:
        ret += 1

    if total == k:
        break

print(ret)
