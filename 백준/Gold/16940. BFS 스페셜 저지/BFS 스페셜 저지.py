from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, tree, visited):
    queue = deque([start])
    visited[start] = True
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)
        for next in tree[current]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    return order


n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visit_order = list(map(int, input().split()))

order_idx = [0] * (n+1)
for idx, node in enumerate(visit_order):
    order_idx[node] = idx

for i in range(1, n+1):
    tree[i].sort(key=lambda x: order_idx[x])

visited = [False] * (n+1)
result = bfs(1, tree, visited)

print(1 if result == visit_order else 0)