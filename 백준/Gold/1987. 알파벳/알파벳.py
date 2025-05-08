import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bound(x, y):
    return 0 <= x < r and 0 <= y < c

def dfs(x, y, visited_mask, current_moves):
    global max_moves
    max_moves = max(max_moves, current_moves)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if in_bound(nx, ny):
            char_index = ord(board[nx][ny]) - ord('A')
            if not (visited_mask & (1 << char_index)):
                dfs(nx, ny, visited_mask | (1 << char_index),current_moves + 1)


r, c = tuple(map(int, input().split()))
board = [list(input().strip()) for _ in range(r)]

start_char = ord(board[0][0]) - ord('A')
max_moves = 0

dfs(0, 0, 1 << start_char, 1)
print(max_moves)