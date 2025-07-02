from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

dp = []
for elem in sequence:
    if len(dp) == 0 or elem > dp[-1]:
        dp.append(elem)
    else:
        idx = bisect_left(dp, elem)
        dp[idx] = elem

print(len(dp))