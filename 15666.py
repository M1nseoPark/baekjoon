n, m = map(int, input().split())
number = list(map(int, input().split()))

number.sort()

def pick(n, picked, toPick):
    if toPick == 0:
        if picked not in printed:
            printed.append(list(picked))
            for i in picked:
                print(i, end=' ')
            print()
            return
        else:
            return

    for i in range(n):
        if len(picked) == 0 or number[i] >= picked[-1]:
            picked.append(number[i])
            pick(n, picked, toPick - 1)
            picked.pop()

printed = []
picked = []
pick(n, picked, m)
