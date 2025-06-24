import sys
input = sys.stdin.readline

n = int(input())
states = [[0 if ch == 'H' else 1 for ch in input().rstrip()] for _ in range(n)]

min_count = float('inf')

for mask in range(2 ** n):
    temp = [row[:] for row in states]

    for row in range(n):
        if mask & (1 << row):
            for col in range(n):
                temp[row][col] ^= 1

    total = 0
    for col in range(n):
        count = 0
        for row in range(n):
            if temp[row][col] == 1:
                count += 1
        total += min(count, n - count)

    min_count = min(min_count, total)

print(min_count)