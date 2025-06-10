from collections import deque
import sys
input = sys.stdin.readline

def bfs(shark_pos, size):
    queue = deque()
    queue.append((shark_pos[0], shark_pos[1], 0))
    visited = [[False]*n for _ in range(n)]
    visited[shark_pos[0]][shark_pos[1]] = True
    candidates = []
    min_dist = None

    while queue:
        x, y, dist = queue.popleft()

        if min_dist is not None and dist > min_dist:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] <= size:
                    visited[nx][ny] = True
                    if 0 < grid[nx][ny] < size:
                        candidates.append((dist + 1, nx, ny))
                        min_dist = dist + 1
                    else:
                        queue.append((nx, ny, dist + 1))
    
    return sorted(candidates)

# 입력 처리
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 초기 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            shark_pos = (i, j)
            grid[i][j] = 0
            break

# 방향: 상, 좌, 하, 우
directions = [(-1,0), (0,-1), (1,0), (0,1)]

# 초기 상어 상태
size = 2
eaten = 0
total_time = 0

# 시뮬레이션
while True:
    candidates = bfs(shark_pos, size)
    if not candidates:
        break

    dist, x, y = candidates[0]
    shark_pos = (x, y)
    total_time += dist
    grid[x][y] = 0
    eaten += 1

    if eaten == size:
        size += 1
        eaten = 0

print(total_time)