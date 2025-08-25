import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

enumerated_arr = [(arr[i], i) for i in range(n)]
enumerated_arr.sort(key=lambda x: x[0])

max_move = 0
for sorted_idx, (val, original_idx) in enumerate(enumerated_arr):
    move = original_idx - sorted_idx
    if move > max_move:
        max_move = move

print(max_move + 1)