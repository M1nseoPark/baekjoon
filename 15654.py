n, m = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
picked = []
def pick(picked, toPick):
    if toPick == 0:
        for i in range(m):
            print(picked[i], end=' ')
        print()

    for i in range(n):
        if A[i] in picked:
            continue
        picked.append(A[i])
        pick(picked, toPick - 1)
        picked.pop(-1)

pick(picked, m)
