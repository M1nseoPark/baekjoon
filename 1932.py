import sys

n = int(sys.stdin.readline())
triangle = []
for i in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

k = 2
for y in range(1, n):
    for x in range(k):
        if x == 0:
            triangle[y][x] += triangle[y-1][x]
        elif x == y:
            triangle[y][x] += triangle[y-1][x-1]
        else:
            triangle[y][x] += max(triangle[y-1][x-1], triangle[y-1][x])
    k += 1

print(max(triangle[n-1]))
