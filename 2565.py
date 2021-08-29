n = int(input())
line = []
for i in range(n):
    line.append(list(map(int, input().split())))

line.sort()

result = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if line[j][1] < line[i][1]:
            result[i] = max(result[i], result[j] + 1)

print(n - max(result))
