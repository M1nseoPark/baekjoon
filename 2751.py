import sys

n = int(sys.stdin.readline())   # input() 사용하면 시간초과
A = []
for i in range(n):
    A.append(int(sys.stdin.readline()))

A.sort()
for i in A:
    print(i)
