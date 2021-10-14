import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tomato = []
for i in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque([])

def bfs():
    while len(q) != 0:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    q.append((nx, ny))


for x in range(n):
    for y in range(m):
        if tomato[x][y] == 1:
            q.append((x, y))

bfs()
make = True
day = -2
for x in range(n):
    for y in range(m):
        if tomato[x][y] == 0:
            make = False
        day = max(day, tomato[x][y])

if not make:
    print('-1')
elif day == -1:
    print('0')
else:
    print(day - 1)
