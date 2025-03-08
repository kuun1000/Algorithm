from collections import deque
import sys
input = sys.stdin.readline


def is_bounds(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def bfs(box, visited, ripes, n, m):
    queue = deque(ripes)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy, day = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_bounds(nx, ny, n, m) and box[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                box[nx][ny] = day + 1
                queue.append((nx, ny, day + 1))



m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ripes = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            ripes.append((i, j, 1))
            visited[i][j] = True

bfs(box, visited, ripes, n, m)

max_day = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            sys.exit(0)
        max_day = max(max_day, box[i][j])
print(max_day - 1)