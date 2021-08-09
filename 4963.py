import sys
sys.setrecursionlimit(800000)

def dfs(y, x):
        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
        dy = [-1, -1, -1, 0, 0, 1, 1, 1]

        visited[y][x] = 1

        for i in range(8):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < w and 0 <= my < h and visited[my][mx] == 0 and map_island[my][mx] == 1:
                dfs(my, mx)
                
while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    map_island = []
    for i in range(h):
        map_island.append(list(map(int, input().split())))

    visited = [[0] * w for i in range(h)]
    island = 0
    
    for i in range(h):
        for j in range(w):
            if map_island[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                island += 1

    print(island)
