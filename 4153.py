while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    A = [a, b, c]
    m = max(A)
    s = 0

    for i in A:
        s += i * i

    if s == (2 * m * m):
        print("right")
    else:
        print("wrong")
