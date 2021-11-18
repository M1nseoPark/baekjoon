t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    A, B = a, b

    while a != 0:
        k = b % a
        b, a = a, k

    print(A * B // b)
