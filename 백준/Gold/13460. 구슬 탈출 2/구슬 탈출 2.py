from collections import deque
import sys
input = sys.stdin.readline

def is_valid(x, y): # 유효 위치인지 확인하기
    return 0 <= x < n and 0 <= y < m

def roll(x, y, dir): # 구슬 굴리기
    is_in_hole = False
    count = 0
    while is_valid(x + dir[0], y + dir[1]):
        nx, ny = x + dir[0], y + dir[1]
        if board[nx][ny] == '#':
            break
        elif board[nx][ny] == 'O':
            x, y = nx, ny
            is_in_hole = True
            break
        x, y = nx, ny
        count += 1
    return x, y, count, is_in_hole

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(rx, ry, bx, by, count):
    queue = deque([((rx, ry), (bx, by), count)])

    while queue:
        red, blue, count = queue.popleft()

        if blue == hole:
            continue
        if red == hole:
            return count + 1
        if count >= 10:
            return -1
        
        for dir in directions:
            nrx, nry, nrcount, r_in_hole = roll(*red, dir)
            nbx, nby, nbcount, b_in_hole = roll(*blue, dir)

            if b_in_hole:
                continue
            if r_in_hole:
                return count + 1

            if nrx == nbx and nry == nby:
                if nrcount > nbcount:
                    nrx, nry = nrx - dir[0], nry - dir[1]
                else:
                    nbx, nby = nbx - dir[0], nby - dir[1]
            
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

print(bfs(*red, *blue, 0))