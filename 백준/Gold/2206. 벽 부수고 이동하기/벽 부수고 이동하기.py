from collections import deque
import sys
input = sys.stdin.readline

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([])
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]

    queue.append([0, 0, 0, 1])  # [x, y, is_break, distance]
    visited[0][0][0] = True

    while queue:
        cx, cy, is_break, distance = queue.popleft()

        if cx == n - 1 and cy == m - 1:
            return distance

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if is_valid(nx, ny) and not visited[nx][ny][is_break]:
                if not grid[nx][ny]:
                    queue.append([nx, ny, is_break, distance + 1])
                    visited[nx][ny][is_break] = True
                
                elif grid[nx][ny] and not is_break:
                    queue.append([nx, ny, 1, distance + 1])
                    visited[nx][ny][1] = True
    return -1
                    

n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs())