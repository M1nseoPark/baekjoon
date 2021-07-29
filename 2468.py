import sys
sys.setrecursionlimit(800000)
from collections import deque

n = int(input())
height = []
high = 0   # 최대 높이
low = 0   # 최소 높이

for i in range(n):
    k = list(map(int, input().split()))
    max_temp = max(k)
    min_temp = min(k)
    if high < max_temp:
        high = max_temp
    if low > min_temp:
        low = min_temp
    height.append(k)

def bfs(y, x, h):
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]

    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    
    while len(q) != 0:
        y, x = q.popleft()

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if 0 <= mx < n and 0 <= my < n and visited[my][mx] == 0 and height[my][mx] > h:
                bfs(my, mx, h)

safe = []    
for h in range(low, high+1):
    visited = [[0] * n for i in range(n)]
    s = 0
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and height[i][j] > h:
                bfs(i, j, h)
                s += 1

    safe.append(s)

print(max(safe))
