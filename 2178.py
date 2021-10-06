n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input().strip())))


def bfs(x, y):
    q = []
    q.append((x, y))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while len(q) != 0:
        x, y = q[0]
        q.pop(0)

        if x == n - 1 and y == m - 1:
            print(visited[x][y])
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maze[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                    
bfs(0, 0)  
