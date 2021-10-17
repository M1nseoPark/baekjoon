n, m, v = map(int, input().split())
adj = [[0] * (n + 1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1
    

visited = [False for _ in range(n+1)]
def dfs(v):
    print(v, end=' ')
    visited[v] = True

    for i in range(1, n+1):
        if (not visited[i]) and adj[v][i] == 1:
            dfs(i)


def bfs(v):
    q = []
    q.append(v)
    visited[v] = False
    while len(q) != 0:
        v = q[0]
        print(v, end=' ')
        q.pop(0)
        for i in range(1, n+1):
            if visited[i] and adj[v][i] == 1:
                q.append(i)
                visited[i] = False


dfs(v)
print()
bfs(v)
