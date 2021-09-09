n = int(input())
line = []
for i in range(n):
    line.append(list(map(int, input().split())))

start = line[0][0]
end = line[0][1]
total = 0
for i in range(1, n):
    if start <= line[i][0] and line[i][1] <= end:
        pass
    elif line[i][0] <= start and end <= line[i][1]:
        start = line[i][0]
        end = line[i][1]
    elif start <= line[i][1] and line[i][0] <= start and line[i][1] <= end:
        start = line[i][0]
    elif start <= line[i][0] and line[i][0] <= end and end <= line[i][1]:
        end = line[i][1]
    else:
        total += (end - start)
        start = line[i][0]
        end = line[i][1]

total += (end - start)
print(total)
