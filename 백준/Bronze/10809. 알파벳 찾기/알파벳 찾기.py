import sys
input = sys.stdin.readline

s = list(input().strip())

result = [-1] * 26

for i, elem in enumerate(s):
    idx = ord(elem) - ord('a')
    if result[idx] == -1:
        result[idx] = i

print(*result)