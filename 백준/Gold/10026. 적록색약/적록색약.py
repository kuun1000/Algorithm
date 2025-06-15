from collections import deque
import sys
input = sys.stdin.readline

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, painting, visited, n):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and painting[cx][cy] == painting[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def count_regions(painting, n):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, painting, visited, n)
                count += 1
    return count

def convert_for_color_weak(painting):
    return [['R' if c == 'G' else c for c in row] for row in painting]

# 입력 처리
n = int(input())
painting = [list(input().rstrip()) for _ in range(n)]

# 일반인과 색약인 경우 처리
normal_count = count_regions(painting, n)
color_weak_painting = convert_for_color_weak(painting)
weak_count = count_regions(color_weak_painting, n)

# 출력
print(normal_count, weak_count)