# 100 x 100 격자
grid = [[0 for _ in range(100)]
        for _ in range(100)]

n = int(input())    # 색종이의 수
positions = [list(map(int, input().split())) for _ in range(n)]   # 색종이 붙인 위치

# 각 색종이에 대해
for position in positions:
    # 좌측 하단 -> 좌측 상단으로 생각
    x, y = position
    
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            grid[i][j] = 1

print(sum(sum(grid, [])))