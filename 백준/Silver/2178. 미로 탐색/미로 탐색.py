from collections import deque
import sys
input = sys.stdin.readline

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    queue = deque([(x, y, 1)])
    visited[x][y] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy, dist = queue.popleft()

        if cx == n - 1 and cy == m - 1:
            return dist

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny) and not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, dist+1))


n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

print(bfs(0, 0))