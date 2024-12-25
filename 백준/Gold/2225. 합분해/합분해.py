n, k = map(int, input().split())

dp = [[0] * (n+1) for _ in range(k+1)]

for n in range(n+1):
    dp[1][n] = 1

for k in range(2, k+1):
    for n in range(n+1):
        dp[k][n] = dp[k-1][n]
        if n > 0:
            dp[k][n] += dp[k][n-1]
        dp[k][n] %= 1000000000

print(dp[k][n])