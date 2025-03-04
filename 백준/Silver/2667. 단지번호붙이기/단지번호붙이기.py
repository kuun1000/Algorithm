from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def bfs(x, y, grid, visited, n):
    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny, n) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1
    return cnt

n = int(input())
grid = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

complexes = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            complexes.append(bfs(i, j, grid, visited, n))

complexes.sort()
print(len(complexes))
for size in complexes:
    print(size)