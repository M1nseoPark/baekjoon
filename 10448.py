T = []
for i in range(1, 46):
    T.append(i * (i + 1) // 2)
    

t = int(input())
for i in range(t):
    k = int(input())
    make = False
    for j in T:
        for w in T:
            if k - j - w in T:
                make = True
                break
            if (k - j - w) <= 0:
                break

    if make:
        print('1')
    else:
        print('0')
