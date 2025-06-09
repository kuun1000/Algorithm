from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while hedgehog:
        # 물의 확장
        for _ in range(len(water)):
            x, y, t = water.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    if grid[nx][ny] != 'X' and grid[nx][ny] != 'D':
                        if time_water[nx][ny] == -1:
                            time_water[nx][ny] = t+1
                            water.append((nx, ny, t+1))
        # 고슴도치 이동
        for _ in range(len(hedgehog)):
            x, y, t = hedgehog.popleft()

            if grid[x][y] == 'D':
                return t
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    if (grid[nx][ny] == 'D' or grid[nx][ny] == '.') and grid[nx][ny] != 'X':
                        if time_water[nx][ny] != -1 and time_water[nx][ny] <= t+1:
                            continue
                        if not visited_hedgehog[nx][ny]:
                            visited_hedgehog[nx][ny] = True
                            hedgehog.append((nx, ny, t+1))
    return 'KAKTUS'



# 입력 처리
r, c = list(map(int, input().split()))
grid = [list(input().rstrip()) for _ in range(r)]

# 위치 파악 및 큐 초기화
hedgehog, water = deque([]), deque([])

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'S':
            hedgehog.append((i, j, 0))
        elif grid[i][j] == 'D':
            beaver = (i, j)
        elif grid[i][j] == '*':
            water.append((i, j, 0))

# 방문 배열 정의
visited_hedgehog = [[False] * c for _ in range(r)]
time_water = [[-1] * c for _ in range(r)]

# 방향 정의
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 결과 출력
print(bfs())