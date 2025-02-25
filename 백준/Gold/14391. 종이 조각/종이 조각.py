n, m = map(int, input().split())
paper = [list(map(int, input())) for _ in range(n)]

max_sum = 0
for mask in range(1 << (n * m)):
    total_sum = 0

    # 가로 조각 숫자
    for i in range(n):
        current_num = 0
        for j in range(m):
            idx = i * m + j
            if mask & (1 << idx):
                current_num = current_num * 10 + paper[i][j]
            else:
                total_sum += current_num
                current_num = 0
        total_sum += current_num
    
    # 세로 조각 숫자
    for j in range(m):
        current_num = 0
        for i in range(n):
            idx = i * m + j
            if not (mask & (1 << idx)):
                current_num =  current_num * 10 + paper[i][j]
            else:
                total_sum += current_num
                current_num = 0
        total_sum += current_num

    max_sum = max(max_sum, total_sum)

print(max_sum)