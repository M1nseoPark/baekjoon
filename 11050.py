n, k = map(int, input().split())
picked = []
ret = 0

def pick(n, picked, toPick):
    if toPick == 0:
        global ret
        ret += 1

    if len(picked) == 0:
        smallest = 1
    else:
        smallest = picked[-1] + 1

    for i in range(smallest, n+1):
        picked.append(i)
        pick(n, picked, toPick - 1)
        picked.remove(i)

pick(n, picked, k)
print(ret)
