import sys
from collections import deque
input = sys.stdin.readline


def is_valid(x, y):
    return 0 <= x < h and 0 <= y < w


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))



while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)