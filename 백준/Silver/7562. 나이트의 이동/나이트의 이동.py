from collections import deque
import sys
input = sys.stdin.readline

def in_bound(x, y, board_size):
    return 0 <= x < board_size and 0 <= y < board_size

def bfs(board_size, start, target):
    visited = [[False] * board_size for _ in range(board_size)]
    sx, sy = start
    tx, ty = target

    queue = deque([(sx, sy, 0)])
    visited[sx][sy] = True

    knight_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                  (-2, 1), (-1, 2), (1, 2), (2, 1)]
    
    while queue:
        sx, sy, moves = queue.popleft()

        if sx == tx and sy == ty:
            return moves

        for dx, dy in knight_moves:
            nx, ny = sx + dx, sy + dy
            if in_bound(nx, ny, board_size) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves+1))
    return 0



def solve():
    board_size = int(input())
    start = tuple(map(int, input().split()))
    target = tuple(map(int, input().split()))

    print(bfs(board_size, start, target))


t = int(input())
for _ in range(t):
    solve()