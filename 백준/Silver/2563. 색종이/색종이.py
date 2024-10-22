grid = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    w, h = tuple(map(int, input().split()))
    for i in range(w, w+10):
        for j in range(h, h+10):
            grid[i][j] = 1
            
print(sum(sum(grid, start=[])))