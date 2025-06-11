from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    # 초기화
    queue = deque([])
    visited = [[ [float('inf')] * 4 for _ in range(w) ] for _ in range(h)]

    sx, sy = lasers[0]  # 시작점
    for d in range(4):
        nx = sx + directions[d][0]
        ny = sy + directions[d][1]
        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != '*':
            queue.append((nx, ny, d, 0))
            visited[nx][ny][d] = 0
    ex, ey = lasers[1]  # 도착점
    
    # BFS 루프
    while queue:
        cx, cy, cd, cm = queue.popleft()

        if (cx, cy) == (ex, ey):
            return min(visited[ex][ey])

        # 직진
        nx, ny = cx + directions[cd][0], cy + directions[cd][1]
        while 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != "*":
            if visited[nx][ny][cd] > cm:
                queue.append((nx, ny, cd, cm))
                visited[nx][ny][cd] = cm
            nx += directions[cd][0]
            ny += directions[cd][1]

        # 회전
        for nd in range(4):
            if nd == cd or (cd // 2 == nd // 2):
                continue
            nx, ny = cx + directions[nd][0], cy + directions[nd][1]
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != '*':
                if visited[nx][ny][cd] > cm:
                    queue.append((nx, ny, nd, cm+1))
                    visited[nx][ny][nd] = cm+1


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
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우

print(bfs())