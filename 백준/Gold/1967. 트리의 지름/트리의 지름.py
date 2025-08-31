from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visited = [False] * (n+1)
    dist = [0] * (n+1)
    queue = deque([start])
    visited[start] = True

    while queue:
        u = queue.popleft()
        for v, w in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + w
                queue.append(v)
    
    max_dist = max(dist)
    far_node = dist.index(max_dist)
    return far_node, max_dist

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    parent, child, weight = list(map(int, input().split()))
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

a, _ = bfs(1)           
_, diameter = bfs(a)    

print(diameter)