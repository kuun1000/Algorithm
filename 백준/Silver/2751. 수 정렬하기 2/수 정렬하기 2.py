import sys
input = sys.stdin.readline

n = int(input())
nums = sorted((int(input()) for _ in range(n)))

print(*nums, sep="\n")