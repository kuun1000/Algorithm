from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    visited[start] = True
    q.append(start)

    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                visited[v] = True
                q.append(v)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
parent = [0] * (n+1)

bfs(1)

for i in range(2, n+1):
    print(parent[i])