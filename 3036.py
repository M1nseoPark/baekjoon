n = int(input())
ring = list(map(int, input().split()))

for i in range(1, n):
    a, b = ring[i], ring[0]

    while b != 0:
        k = a % b
        a, b = b, k

    print(str(ring[0]//a) + "/" + str(ring[i]//a))
