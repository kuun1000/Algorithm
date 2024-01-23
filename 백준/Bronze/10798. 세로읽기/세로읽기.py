# 5 x n 격자 입력 받기
grid = [input() for _ in range(5)]

for j in range(15):     # 각 행에 대해
    for i in range(5):      # 각 열에 대해 
        if j < len(grid[i]):    # 행 인덱스 < 행 원소 개수
            print(grid[i][j], end="")   # 해당 원소 출력