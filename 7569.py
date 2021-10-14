import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
tomato = [[] for i in range(h)]
for i in range(h):
    for j in range(n):
        tomato[i].append(list(map(int, sys.stdin.readline().split())))

dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
q = deque([])
visited = [[[0] * m for i in range(n)] for j in range(h)]
def bfs():
    while len(q) != 0:
        x, y, z = q.popleft()
        visited[z][x][y] = 1

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if tomato[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    tomato[nz][nx][ny] = tomato[z][x][y] + 1
                    q.append((nx, ny, nz))
                    visited[nz][nx][ny] = 1


for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 1:
                q.append((x, y, z))

bfs()
make = True
day = -2
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 0:
                make = False
            day = max(day, tomato[z][x][y])

if not make:
    print('-1')
else:
    print(day - 1)
