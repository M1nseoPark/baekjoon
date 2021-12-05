n, m = map(int, input().split())
picked = []

def pick(n, picked, toPick):
    if toPick == 0:
        for i in picked:
            print(i, end=' ')
        print()
        return

    if len(picked) == 0:
        smallest = 1
    else:
        smallest = picked[-1] + 1   # 리스트 맨 뒤 원소: 리스트[-1]

    for i in range(smallest, n+1):
        picked.append(i)
        pick(n, picked, toPick - 1)
        picked.remove(i)

pick(n, picked, m)
