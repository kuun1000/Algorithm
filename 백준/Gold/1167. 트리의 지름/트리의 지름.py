from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    visited = [False] * (v + 1)
    distance = [0] * (v + 1)

    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        for neighbor, dist in tree[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + dist
                queue.append(neighbor)

    max_dist = max(distance)
    farthest_node = distance.index(max_dist)

    return farthest_node, max_dist


v = int(input())
tree = {}

for _ in range(v):
    data = list(map(int, input().split()))
    node = data[0]
    tree[node] = []

    i = 1
    while data[i] != -1:
        neighbor = data[i]
        dist = data[i+1]
        tree[node].append((neighbor, dist))

        if neighbor not in tree:
            tree[neighbor] = []
        tree[neighbor].append((node, dist))

        i += 2

u, _ = bfs(1)
_, d = bfs(u)

print(d)