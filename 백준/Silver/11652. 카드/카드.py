import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

d = {}
for elem in arr:
    if elem not in d:
        d[elem] = 1
    else:
        d[elem] += 1

sorted_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

print(sorted_d[0][0])