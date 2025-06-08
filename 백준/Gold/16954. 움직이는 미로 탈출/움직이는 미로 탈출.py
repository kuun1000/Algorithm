from collections import deque

# 8x8 방향: 상, 하, 좌, 우, 대각선(왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래) + 제자리
dx = [-1, 1, 0, 0, -1, -1, 1, 1, 0]
dy = [0, 0, -1, 1, -1, 1, -1, 1, 0]

def move_walls(board):
    # 벽을 한 칸 아래로 내리기
    new_board = [['.'] * 8 for _ in range(8)]
    for i in range(7):
        for j in range(8):
            if board[i][j] == '#':
                new_board[i + 1][j] = '#'
    # 7번째 줄은 없어지고, 0번째 줄은 새로 빈칸으로 초기화
    return new_board

def solve(board):
    queue = deque()
    queue.append((7, 0, 0))  # (x, y, time)

    visited = [[[False] * 9 for _ in range(8)] for _ in range(8)]
    visited[7][0][0] = True

    while queue:
        x, y, t = queue.popleft()
        if (x, y) == (0, 7):
            return 1  # 오른쪽 위 도착!

        if t >= 8:  # 벽이 다 내려갔을 경우
            return 1

        for dir in range(9):
            nx = x + dx[dir]
            ny = y + dy[dir]
            nt = min(t + 1, 8)

            if 0 <= nx < 8 and 0 <= ny < 8:
                if nx - t >= 0 and board[nx - t][ny] == '#':
                    continue  # 현재 시간에 벽이 있으면 못감
                if nx - (t + 1) >= 0 and board[nx - (t + 1)][ny] == '#':
                    continue  # 다음 시간에 벽이 내려올 위치도 체크
                if not visited[nx][ny][nt]:
                    visited[nx][ny][nt] = True
                    queue.append((nx, ny, nt))
            else:
                continue  # 범위를 벗어나면 패스

    return 0  # 큐가 빌 때까지 도착하지 못했다면 실패

# 입력 받기
board = [list(input().strip()) for _ in range(8)]

print(solve(board))