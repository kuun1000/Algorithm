from collections import deque

def dfs(v, graph, visited, result):
    visited[v] = True
    result.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, graph, visited, result)

def bfs(v, graph, visited, result):
    queue = deque([v])
    visited[v] = True
    result.append(v)

    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                result.append(i)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [False] * (n+1)
result = []
dfs(v, graph, visited, result)
print(' '.join(map(str, result)))

visited = [False] * (n+1)
result = []
bfs(v, graph, visited, result)
print(' '.join(map(str, result)))