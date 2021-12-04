n, m = map(int, input().split())
picked = []

def pick(n, picked, toPick):
    if toPick == 0:
        for i in picked:
            print(i, end=' ')
        print()
        return

    for i in range(1, n+1):
        picked.append(i)
        pick(n, picked, toPick - 1)
        picked.pop(-1)

pick(n, picked, m)
