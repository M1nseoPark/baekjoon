n, k = map(int, input().split())
thing = [[0, 0]]
for i in range(n):
    thing.append(list(map(int, input().split())))

p = [[0] * (k + 1) for i in range(n + 1)]

for i in range(1, n+1):
    for j in range(k, 0, -1):
        if j - thing[i][0] >= 0:
            p[i][j] = max(p[i - 1][j], thing[i][1] + p[i - 1][j - thing[i][0]])
        else:
            p[i][j] = p[i - 1][j]

print(max(p[n]))
