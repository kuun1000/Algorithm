n, m = tuple(map(int, input().split()))

# 바구니의 번호
basket = [i for i in range(1, n+1)]

# 각 명령에 대해
for _ in range(m):
    i, j = tuple(map(int, input().split()))

    # 범위에 해당하는 부분을 뒤집음
    basket[i-1:j] = basket[i-1:j][::-1] 

print(*basket)