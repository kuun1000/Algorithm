A, B = tuple(map(int, input().split()))
C = int(input())

current_time = A * 60 + B
expect_time = current_time + C

H, M = expect_time // 60, expect_time % 60

if H >= 24:
    H -= 24
    
print(f"{H} {M}")