from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    # 초기화
    queue = deque([])
    visited = [[[False] * 4 for _ in range(w)] for _ in range(h)]

    sx, sy = lasers[0]  # 시작점
    for d in range(4):
        nx = sx + dir[d][0]
        ny = sy + dir[d][1]
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != '*':
            queue.append((nx, ny, d, 0))
            visited[nx][ny][d] = True
    ex, ey = lasers[1]  # 도착점
    
    # BFS 루프
    while queue:
        cx, cy, cd, cm = queue.popleft()

        if (cx, cy) == (ex, ey):
            return cm

        # 직진
        nx, ny = cx + dir[cd][0], cy + dir[cd][1]
        while 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != "*":
            if not visited[nx][ny][cd]:
                queue.append((nx, ny, cd, cm))
                visited[nx][ny][cd] = True
            nx += dir[cd][0]
            ny += dir[cd][1]

        # 회전
        if cd in [0, 1]:
            for nd in [2, 3]:
                nx = cx + dir[nd][0]
                ny = cy + dir[nd][1]
                if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != "*":
                    if not visited[nx][ny][nd]:
                        queue.append((nx, ny, nd, cm+1))
                        visited[nx][ny][nd] = True
        elif cd in [2, 3]:
            for nd in [0, 1]:
                nx = cx + dir[nd][0]
                ny = cy + dir[nd][1]
                if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != "*":
                    if not visited[nx][ny][nd]:
                        queue.append((nx, ny, nd, cm+1))
                        visited[nx][ny][nd] = True
        



# 입력 처리
w, h = list(map(int, input().split()))
grid = [list(input().rstrip()) for _ in range(h)]

# 레이저 위치 탐색
lasers = []
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'C':
            lasers.append((i, j))

# 방향 정의 
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우

print(bfs())