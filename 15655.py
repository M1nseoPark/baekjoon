n, m = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

def pick(picked, toPick):
    if toPick == 0:
        for i in range(m):
            print(picked[i], end=' ')
        print()

    for i in range(n):
        if A[i] in picked:
            continue
        if len(picked) != 0 and A[i] < picked[-1]:
            continue
        picked.append(A[i])
        pick(picked, toPick - 1)
        picked.pop(-1)

picked = []
pick(picked, m)
