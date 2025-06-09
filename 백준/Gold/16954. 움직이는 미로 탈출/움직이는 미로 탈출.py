from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(7, 0, 0)])  # x, y, time
    visited[7][0][0] = True

    while queue:
        x, y, t = queue.popleft()

        # 목표 위치에 도달
        if (x, y) == (0, 7):
            return 1
        
        # 벽이 모두 내려간 경우
        if t > 8:
            return 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            nt = min(t+1, 8)

            if 0 <= nx < 8 and 0 <= ny < 8: # 보드 내의 위치인지 확인
                # 현재 칸에 벽이 있는 경우 갈 수 없음
                if nx - t >= 0 and board[nx-t][ny] == '#':
                    continue
                # 다음 시간에 벽이 있는 경우 갈 수 없음
                if (nx - (t + 1)) >= 0 and board[nx-(t+1)][ny] == '#':
                    continue
                if not visited[nx][ny][nt]:
                    visited[nx][ny][nt] = True
                    queue.append((nx, ny, nt))
            else:
                continue
    return 0


board = [list(input().rstrip()) for _ in range(8)]

directions = [
    (-1, 0), (-1, 1), (-1, -1),
    (0, 0), (0, 1), (0, -1), 
    (1, 0), (1, 1), (1, -1) 
]
visited = [[[False] * 9 for _ in range(8)] for _ in range(8)]

print(bfs())