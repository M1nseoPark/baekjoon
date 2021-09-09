import sys

t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    A.sort()
    B.sort()

    result = 0
    for i in range(n):
        eat = False
        for j in range(m):
            if A[i] <= B[j]:
                eat = True
                result += j
                break

        if not eat:
            result += m

    print(result)
