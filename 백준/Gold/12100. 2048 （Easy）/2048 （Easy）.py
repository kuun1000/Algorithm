from enum import Enum
import sys
import copy
input = sys.stdin.readline

# 방향 정의
class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

# 한 줄 처리 함수
def process_line(line):
    new_line = [num for num in line if num != 0]
    result = []
    i = 0
    while i < len(new_line):
        if i < len(new_line) - 1 and new_line[i] == new_line[i+1]:
            result.append(new_line[i] * 2)
            i += 2
        else:
            result.append(new_line[i])
            i += 1
    result.extend([0] * (len(line) - len(result)))
    return result

# 보드 전치
def transpose_board(board):
    return [[board[j][i] for j in range(n)] for i in range(n)]

# 각 행 뒤집기
def reverse_board(board):
    return [row[::-1] for row in board]

# 보드를 이동시키는 함수
def move_board(board, direction):
    if direction == Direction.LEFT:
        return [process_line(row) for row in board]

    elif direction == Direction.RIGHT:
        reversed_board = reverse_board(board)
        processed_board = [process_line(row) for row in reversed_board]
        return reverse_board(processed_board)

    elif direction == Direction.UP:
        transposed_board = transpose_board(board)
        processed_board = [process_line(row) for row in transposed_board]
        return transpose_board(processed_board)

    elif direction == Direction.DOWN:
        transposed_board = transpose_board(board)
        reversed_board = reverse_board(transposed_board)
        processed_board = [process_line(row) for row in reversed_board]
        return transpose_board(reverse_board(processed_board))

# DFS를 통한 최대 블록 탐색
def dfs(board, depth):
    max_block = max(max(row) for row in board)

    if depth >= 5:
        return max_block

    max_value = max_block
    for direction in Direction:
        new_board = move_board(board, direction)
        if tuple(map(tuple, new_board)) != tuple(map(tuple, board)):
            max_value = max(max_value, dfs(new_board, depth + 1))
    return max_value

# 입력 처리
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 최댓값 초기화 및 DFS 시작
max_num = 0
print(dfs(board, 0))