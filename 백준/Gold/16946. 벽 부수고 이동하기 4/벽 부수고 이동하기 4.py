from collections import deque
import sys
input = sys.stdin.readline

def in_grid(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y, id):
    queue = deque([(x, y)])
    visited[x][y] = True
    group_map[x][y] = group_id
    count = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if in_grid(nx, ny) and not visited[nx][ny] and not grid[nx][ny]:
                visited[nx][ny] = True
                group_map[nx][ny] = group_id
                queue.append((nx, ny))
                count += 1

    return count

n, m = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(n)]

group_map = [[-1] * m for _ in range(n)]
group_size = []
visited = [[False] * m for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 0 영역 그룹화
group_id = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and not grid[i][j]:
            size = bfs(i, j, group_id)
            group_size.append(size)
            group_id += 1

# 결과 계산
result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j]:
            unique_groups = set()
            total = 1
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if in_grid(ni, nj):
                    g_id = group_map[ni][nj]
                    if g_id != -1:
                        unique_groups.add(g_id)
            for g in unique_groups:
                total += group_size[g]
            result[i][j] = total % 10

for row in result:
    print("".join(map(str, row)))