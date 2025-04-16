import sys
input = sys.stdin.readline


n = int(input())
s = list(map(int, input().split()))

s.sort()
target = 1

for num in s:
    if num > target:
        break
    target += num

print(target)