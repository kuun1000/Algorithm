import sys
input = sys.stdin.readline



def dfs(node, tree, visited, result):
    visited[node] = True
    result.append(node)

    for i in tree[node]:
        if not visited[i]:
            dfs(i, tree, visited, result)



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
result = []
dfs(1, tree, visited, result)

print(1 if result == visit_order else 0)