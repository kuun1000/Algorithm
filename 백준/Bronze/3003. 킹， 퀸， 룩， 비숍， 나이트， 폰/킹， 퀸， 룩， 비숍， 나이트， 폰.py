# 올바른 피스
piece = [1, 1, 2, 2, 2, 8]
# 발견한 흰색 피스 
white_piece = list(map(int, input().split()))

# 올바른 피스 - 발견한 흰색 피스
print(*[p - wp for p, wp in zip(piece, white_piece)])