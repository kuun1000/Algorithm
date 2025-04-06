from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs(start):
    visited = [False] * (n+1)
    distance = [0] * (n+1)

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


n = int(input())
tree = defaultdict(list)

for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

u, _ = bfs(1)
_, d = bfs(u)

print(d)