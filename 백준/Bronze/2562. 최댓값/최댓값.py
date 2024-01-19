# 9개의 자연수 입력 받기
arr = [int(input()) for _ in range(9)]

# 최댓값
max_val = max(arr)
# 최댓값의 인덱스 + 1
max_idx = arr.index(max_val) + 1

print(max_val)
print(max_idx)