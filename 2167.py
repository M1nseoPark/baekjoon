n, m = map(int, input().split())
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 부분합 배열 구하기
sn = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n+1):
  for j in range(1, m+1):
    sn[i][j] = array[i-1][j-1] + sn[i][j-1] + sn[i-1][j] - sn[i-1][j-1]

k = int(input())
for i in range(k):
  i, j, x, y = map(int, input().split())
  print(sn[x][y] - sn[x][j-1] - sn[i-1][y] + sn[i-1][j-1])
