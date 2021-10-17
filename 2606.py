n = int(input())
m = int(input())
adj = [[0] * (n + 1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

result = 0    
visited = [False for _ in range(n+1)]

def dfs(v):
    global result
    result += 1
    visited[v] = True

    for i in range(1, n+1):
        if (not visited[i]) and adj[v][i] == 1:
            dfs(i)


dfs(1)
print(result - 1)
