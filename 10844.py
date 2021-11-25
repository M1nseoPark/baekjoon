n = int(input())
stair = [[0] * 10 for i in range(101)]

for i in range(1, 10):
    stair[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            stair[i][j] = stair[i-1][j+1]

        elif j == 9:
            stair[i][j] = stair[i-1][j-1]

        else:
            stair[i][j] = stair[i-1][j-1] + stair[i-1][j+1]

result = 0
for i in range(10):
    result += stair[n][i]

print(result % 1000000000)
