while True:
    A = list(map(int, input().split()))

    if A[0] == 0:
        break

    def pick(picked, toPick):
        if toPick == 0:
            for i in range(6):
                print(picked[i], end=' ')
            print()

        if len(picked) == 0:
            smallest = 1
        else:
            smallest = A.index(picked[-1]) + 1

        for i in range(smallest, A[0]+1):
            if A[i] in picked:
                continue
            if len(picked) != 0 and A[i] < picked[-1]:
                continue
            picked.append(A[i])
            pick(picked, toPick - 1)
            picked.pop(-1)

    picked = []
    pick(picked, 6)
    print()
