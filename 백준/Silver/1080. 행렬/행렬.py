import sys
input = sys.stdin.readline

def flip(matrix, i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            matrix[x][y] = '1' if matrix[x][y] == '0' else '0'

def solve(n, m, matrix_a, matrix_b):
    count = 0
    for i in range(n - 2):
        for j in range(m - 2):
            if matrix_a[i][j] != matrix_b[i][j]:
                flip(matrix_a, i, j)
                count += 1
    return count if matrix_a == matrix_b else -1

n, m = tuple(map(int, input().split()))
matrix_a = [list(input().rstrip()) for _ in range(n)]
matrix_b = [list(input().rstrip()) for _ in range(n)]

print(solve(n, m, matrix_a, matrix_b))