t = int(input())

for k in range(t):
    k = int(input())
    n = int(input())
    live = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    for i in range(k):
        for j in range(1, n):
            live[j] = live[j] + live[j-1]

    print(live[n-1])
