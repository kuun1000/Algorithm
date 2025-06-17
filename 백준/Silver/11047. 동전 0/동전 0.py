import sys
input = sys.stdin.readline

n, k = tuple(map(int, input().split()))
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

total = 0
for coin in coins:
    if k == 0:
        break
    cnt = k // coin
    total += cnt
    k -= cnt * coin

print(total)