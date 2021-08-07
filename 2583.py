from collections import deque

m, n, k = map(int, input().split())
paper = [[0] * n for i in range(m)]
for i in range(k):
  part = list(map(int, input().split()))

  for j in range(part[1], part[3]):   # *
    for k in range(part[0], part[2]):
      paper[j][k] = 1

def bfs(y, x):
  global answer
  
  # 대각선은 탐색하지 않아도 됨
  dx = [0, -1, 1, 0]
  dy = [-1, 0, 0, 1]

  q = deque()
  q.append((y, x))
  paper[y][x] = 1

  d = 1
  while len(q) != 0:
    y, x = q.popleft()
    for i in range(4):
      mx = x + dx[i]
      my = y + dy[i]
      if 0 <= mx < n and 0 <= my < m and paper[my][mx] == 0:
        q.append((my, mx))
        paper[my][mx] = 1
        d += 1

  answer.append(d)

answer = []
d = 0
for i in range(m):
  for j in range(n):
    if paper[i][j] == 0:
      bfs(i, j)

answer.sort()
print(len(answer))
for i in answer:
  print(i, end=' ')
