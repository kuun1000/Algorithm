n, m = tuple(map(int, input().split()))

# 각 바구니에 들어있는 공의 번호
basket = [0] * n

# m개의 명령에 대해
for _ in range(m):
    # 각 명령을 입력 받음
    i, j, k = tuple(map(int, input().split()))
    
    # i-1 ~ j까지의 원소의 값을 k로 변경
    basket[i-1:j] = [k] * (j - i + 1)
    
print(*basket)