from collections import deque

m, n = map(int, input().split())
banner = []
for i in range(m):
  banner.append(list(input().split()))

visited = [[0] * n for i in range(m)]
answer = 0

def bfs(y, x):
  dx = [-1, 0, 1, -1, 1, -1, 0, 1]
  dy = [-1, -1, -1, 0, 0, 1, 1, 1]

  q = deque()
  q.append((y, x))

  visited[y][x] = 1
  while len(q) != 0:
    y, x = q.popleft()
    for i in range(8):
      mx = x + dx[i]
      my = y + dy[i]
      if 0 <= mx < n and 0 <= my < m and visited[my][mx] == 0 and banner[my][mx] == '1':
        q.append((my, mx))
        visited[my][mx] = 1
  
for i in range(m):
  for j in range(n):
    if visited[i][j] == 0 and banner[i][j] == '1':
      bfs(i, j)
      answer += 1

print(answer)
