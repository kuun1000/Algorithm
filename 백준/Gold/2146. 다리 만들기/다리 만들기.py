import sys
from collections import deque
input = sys.stdin.readline



n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1. 섬에 번호 붙이기
island_label = 2
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs_label(x, y, label):
    queue = deque([(x, y)])
    grid[x][y] = label

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = label
                queue.append((nx, ny))

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bfs_label(i, j, island_label)
            island_label += 1

# 2. 각 섬에서 출발하는 최단 다리 길이 탐색
dist = [[-1] * n for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            dist[i][j] = 0
            queue.append((i, j))

result = sys.maxsize

while queue:
    cx, cy = queue.popleft()
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < n and 0 <= ny < n:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[cx][cy] + 1
                grid[nx][ny] = grid[cx][cy]
                queue.append((nx, ny))
            elif grid[nx][ny] != grid[cx][cy]:
                result = min(result, dist[cx][cy] + dist[nx][ny])
print(result)