import sys

def tsp(cur, cnt, cost):
    global min_cost
    
    if cnt == n and w[cur][0] != 0:
        min_cost = min(min_cost, cost + w[cur][0])
        return min_cost

    if cost >= min_cost:
        return 

    for nxt in range(n):
        if not visited[nxt] and w[cur][nxt] != 0:
            visited[nxt] = True
            tsp(nxt, cnt + 1, cost + w[cur][nxt])
            visited[nxt] = False





n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
visited[0] = True
min_cost = sys.maxsize

tsp(0, 1, 0)
print(min_cost)