from collections import deque
import sys
input = sys.stdin.readline


def find_coins():
    coins = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'o':
                coins.append((i, j))
    return coins

def in_bound(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque()
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

    x1, y1 = coins[0]
    x2, y2 = coins[1]
    q.append((x1, y1, x2, y2, 0))
    visited[x1][y1][x2][y2] = True

    while q:
        x1, y1, x2, y2, cnt = q.popleft()

        if cnt >= 10:
            break

        for dx, dy in directions:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy

            fall1 = not in_bound(nx1, ny1)
            fall2 = not in_bound(nx2, ny2)

            if fall1 and not fall2:
                return cnt + 1
            if fall2 and not fall1:
                return cnt + 1
            if fall1 and fall2:
                continue

            if not fall1 and board[nx1][ny1] == "#":
                nx1, ny1 = x1, y1
            if not fall2 and board[nx2][ny2] == "#":
                nx2, ny2 = x2, y2

            if not visited[nx1][ny1][nx2][ny2]:
                visited[nx1][ny1][nx2][ny2] = True
                q.append((nx1, ny1, nx2, ny2, cnt+1))
    return -1


# 입력 처리
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

# 초기 동전 위치 찾기
coins = find_coins()

# 최소 횟수 구하기
print(bfs())