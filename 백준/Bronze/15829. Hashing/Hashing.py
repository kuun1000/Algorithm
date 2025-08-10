import sys
input = sys.stdin.readline

l = int(input())
arr = list(map(lambda x:ord(x)-96, input().strip()))
r, m = 31, 1234567891

result = 0
for idx, elem in enumerate(arr):
    result += elem * (r**idx)

print(result % m)