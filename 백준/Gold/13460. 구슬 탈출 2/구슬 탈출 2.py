from collections import deque
import sys
input = sys.stdin.readline



def roll(x, y, dx, dy):
    count = 0
    while True:
        nx, ny = x + dx, y + dy
        if board[nx][ny] == '#':
            break
        if board[nx][ny] == 'O':
            return nx, ny, count, True
        x, y = nx, ny
        count += 1
    return x, y, count, False

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(rx, ry, bx, by):
    queue = deque([((rx, ry), (bx, by), 0)])
    visited[rx][ry][bx][by] = True

    while queue:
        (rx, ry), (bx, by), count = queue.popleft()

        if count >= 10:
            return -1

        for dx, dy in directions:
            nrx, nry, r_dist, red_in = roll(rx, ry, dx, dy)
            nbx, nby, b_dist, blue_in = roll(bx, by, dx, dy)

            if blue_in:
                continue
            if red_in:
                return count + 1

            if nrx == nbx and nry == nby:
                if r_dist > b_dist:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append(((nrx, nry), (nbx, nby), count + 1))
    return -1



# 입력 처리 및 상태 초기화
n, m = tuple(map(int, input().split()))
board = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        current = board[i][j]
        if current == 'R':  red = (i, j)
        elif current == 'B': blue = (i, j)
        elif current == 'O': hole = (i, j)

visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
visited[red[0]][red[1]][blue[0]][blue[1]] = True

print(bfs(*red, *blue))