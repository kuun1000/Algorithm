import sys

# 9 x 9 격자판 입력 받기
grid = [list(map(int, input().split())) for _ in range(9)]

# 최댓값 및 최댓값의 인덱스
max_val = -sys.maxsize
max_row, max_col = 0, 0

for i in range(9):
    for j in range(9):
        # 현재 값이 최댓값보다 큰 경우
        if max_val < grid[i][j]:
            max_val = grid[i][j]        # 최댓값 갱신
            max_row, max_col = i, j     # 최댓값의 인덱스 갱신

print(max_val)
print(max_row + 1, max_col + 1)