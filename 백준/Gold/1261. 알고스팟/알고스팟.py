from collections import deque
import sys
input = sys.stdin.readline

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs():
    costs = [[sys.maxsize] * m for _ in range(n)]
    costs[0][0] = 0

    queue = deque([(0, 0)])
    
    while queue:
        cx, cy = queue.popleft()

        if cx == (n - 1) and cy == (m - 1):
            return costs[cx][cy]
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                cost = costs[cx][cy] + 1 if maze[nx][ny] == 1 else costs[cx][cy]
                if cost < costs[nx][ny]:
                    costs[nx][ny] = cost
                    if maze[nx][ny] == 0:
                        queue.appendleft((nx, ny))
                    else:
                        queue.append((nx, ny))
    return 0


m, n = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

print(bfs())