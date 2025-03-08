from collections import deque
import sys

def bfs_tomato(grid, M, N):
    queue = deque()
    days = -1  # BFS 레벨(일 수) 추적
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동

    # 1. 익은 토마토 위치를 큐에 추가
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                queue.append((i, j, 0))  # (세로 위치, 가로 위치, 경과 일수)

    # 2. BFS 수행
    while queue:
        x, y, day = queue.popleft()
        days = max(days, day)  # 최대 일수 업데이트

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                grid[nx][ny] = 1  # 익음 처리
                queue.append((nx, ny, day + 1))

    # 3. 모든 토마토가 익었는지 확인
    for row in grid:
        if 0 in row:
            return -1  # 익지 않은 토마토가 남아 있으면 실패

    return days

# 입력 처리
M, N = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 결과 출력
print(bfs_tomato(grid, M, N))