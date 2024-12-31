MOD = 10007

n = int(input())

dp = [[0] * 10 for _ in range(n+1)]
dp[1] = [1] * 10

for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j] if j > 0 else dp[i-1][0]) % MOD

print(sum(dp[n]) % MOD)