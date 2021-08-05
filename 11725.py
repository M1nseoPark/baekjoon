from collections import deque
import sys
sys.setrecursionlimit(10000000)

n = int(sys.stdin.readline())
tree = [[] for i in range(n+1)]
for i in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  tree[a].append(b)
  tree[b].append(a)

parents = [0 for i in range(n+1)]

def dfs(start, parents):
  for i in tree[start]:
    if parents[i] == 0:
      parents[i] = start
      dfs(i, parents)

dfs(1, parents)

for i in range(2, n+1):
  print(parents[i])
