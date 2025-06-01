from collections import deque
import sys
input = sys.stdin.readline

def in_grid(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([])
    visited = [[[False] * (k+1) for _ in range(m)] for _ in range(n)]

    queue.append([0, 0, 0, 1])
    visited[0][0][0] = True

    while queue:
        cx, cy, broken, distance = queue.popleft()

        if cx == n - 1 and cy == m - 1:
            return distance
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if in_grid(nx, ny) and not visited[nx][ny][broken]:
                if not grid[nx][ny]:
                    queue.append([nx, ny, broken, distance+1])
                    visited[nx][ny][broken] = True
                elif grid[nx][ny] and broken < k and not visited[nx][ny][broken+1]:
                    queue.append([nx, ny, broken + 1, distance+1])
                    visited[nx][ny][broken+1] = True
    return -1

n, m, k = tuple(map(int, input().split()))
grid = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs())