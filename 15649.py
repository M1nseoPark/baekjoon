n, m = map(int, input().split())
picked = []

def pick(n, picked, toPick):
    if toPick == 0:
        for i in picked:
            print(i, end=' ')
        print()
        return

    for i in range(1, n+1):
        if i in picked:
            continue
        picked.append(i)
        pick(n, picked, toPick - 1)
        picked.remove(i)

pick(n, picked, m)
