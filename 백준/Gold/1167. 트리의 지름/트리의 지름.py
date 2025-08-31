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

for _ in range(n):
    data = list(map(int, input().split()))
    u = data[0]
    i = 1
    while data[i] != -1:
        v = data[i]
        w = data[i+1]
        graph[u].append((v, w))
        i += 2

a, _ = bfs(1)           # 임의 노드에서 가장 먼 노드 A 찾기
_, diameter = bfs(a)    # A에서 가정 먼 노드까지 거리(지름)

print(diameter)