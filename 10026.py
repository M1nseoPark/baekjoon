from collections import deque

n = int(input())
drawing = []
for i in range(n):
  data = list(input())
  drawing.append(data)

can = 0
cant = 0

visited = [[0] * n for i in range(n)]

def bfs(y, x):
  dx = [0, -1, 1, 0]
  dy = [-1, 0, 0, 1]

  q = deque()
  q.append((y, x))
  visited[y][x] == 1

  while len(q) != 0:
    y, x = q.popleft()
    
    for i in range(4):
      mx = x + dx[i]
      my = y + dy[i]

      if 0 <= mx < n and 0 <= my < n and visited[my][mx] == 0 and drawing[my][mx] == drawing[y][x]:
        q.append((my, mx))
        visited[my][mx] = 1
    
for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      bfs(i, j)
      can += 1

visited = [[0] * n for i in range(n)]
for i in range(n):
  for j in range(n):
    if drawing[i][j] == 'R':
      drawing[i][j] = 'G'

for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      bfs(i, j)
      cant += 1

print(can, cant)
