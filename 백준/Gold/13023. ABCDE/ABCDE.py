def dfs(node, depth):
    global found
    if found:
        return 
    
    if depth == 4:
        found = True
        return
    
    for friend in relations[node]:
        if not visited[friend]:
            visited[friend] = True
            dfs(friend, depth+1)
            visited[friend] = False



n, m = map(int, input().split())
relations = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

found = False
visited = [False] * n

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(1 if found else 0)