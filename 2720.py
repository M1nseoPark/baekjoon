t = int(input())
for i in range(t):
    c = int(input())

    q = 0
    d = 0
    n = 0
    p = 0
    while c != 0:
        if c >= 25:
            q += c // 25
            c = c % 25

        if c >= 10:
            d += c // 10
            c = c % 10

        if c >= 5:
            n += c // 5
            c = c % 5

        if c >= 1:
            p += c // 1
            c = c % 1

    print(q, d, n, p)
