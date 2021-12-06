import sys

n = int(sys.stdin.readline())
B = [0 for i in range(10000+1)]

for i in range(n):
    B[int(sys.stdin.readline())] += 1

for i in range(10000+1):
    if B[i] == 0:
        continue

    for j in range(B[i]):
        print(i)
