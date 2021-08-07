from collections import deque

r, c = map(int, input().split())
yard = []
for i in range(r):
  yard.append(list(input()))

visited = [[0] * c for i in range(r)]
sheep, wolf = 0, 0

def bfs(y, x):
  global sheep, wolf
  
  dx = [0, -1, 1, 0]
  dy = [-1, 0, 0, 1]
            
  q = deque()
  q.append((y, x))
  visited[y][x] = 1

  s, w = 0, 0
  if yard[y][x] == 'o':
    s += 1

  if yard[y][x] == 'v':
    w += 1
  
  while len(q) != 0:
    y, x = q.popleft()
    for i in range(4):
      mx = x + dx[i]
      my = y + dy[i]

      if 0 <= mx < c and 0 <= my < r and visited[my][mx] == 0:
        if yard[my][mx] == '.' or yard[my][mx] == 'v' or yard[my][mx] == 'o':
          q.append((my, mx))
          visited[my][mx] = 1

          if yard[my][mx] == 'o':
            s += 1

          if yard[my][mx] == 'v':
            w += 1

  if s > w:
    sheep += s
  else:
    wolf += w
    
for i in range(r):
  for j in range(c):
    if visited[i][j] == 0:
      if yard[i][j] == '.' or yard[i][j] == 'v' or yard[i][j] == 'o':
        bfs(i, j)

print(sheep, wolf)
