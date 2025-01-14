def swap(board, x1, y1, x2, y2):
    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]


def check_max(board, n):
    max_length = 1

    # 행 검사
    for i in range(n):
        count = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                count += 1
                max_length = max(max_length, count)
            else:
                count = 1

    # 열 검사
    for j in range(n):
        count = 1
        for i in range(1, n):
            if board[i][j] == board[i-1][j]:
                count += 1
                max_length = max(max_length, count)
            else:
                count = 1

    return max_length
    

def max_candy(board, n):
    max_candies = 0

    for i in range(n):
        for j in range(n):
            # 오른쪽과 교환
            if j + 1 < n and board[i][j] != board[i][j + 1]:
                swap(board, i, j, i, j + 1)
                max_candies = max(max_candies, check_max(board, n))
                swap(board, i, j, i, j + 1)

            # 아래쪽과 교환
            if i + 1 < n and board[i][j] != board[i + 1][j]:
                swap(board, i, j, i + 1, j)
                max_candies = max(max_candies, check_max(board, n))
                swap(board, i, j, i + 1, j)
    
    return max_candies



n = int(input())
candy = [list(input().strip()) for _ in range(n)]

print(max_candy(candy, n))