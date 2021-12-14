t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())

    x = n // h + 1
    y = n % h

    if n % h == 0:
        y = h
        x -= 1

    if x < 10:
        print(str(y) + "0" + str(x))
    else:
        print(str(y) + str(x))
