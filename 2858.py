r, b = map(int, input().split())

for i in range(1, 2500):
    for j in range(1, i+1):
        if (i - 2) * (j - 2) == b and (i * j - b) == r:   // b 개수뿐만 아니라 r 개수도 고려해야 함
            print(str(i) + " " + str(j))
            break
