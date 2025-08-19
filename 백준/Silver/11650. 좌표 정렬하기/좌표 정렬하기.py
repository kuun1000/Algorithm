import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

sorted_arr = sorted(arr, key=lambda x: (x[0], x[1]))

for elem in sorted_arr:
    print(*elem)