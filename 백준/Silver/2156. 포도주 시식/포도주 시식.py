n = int(input())
wines = [int(input()) for _ in range(n)]

if n == 1:
    print(wines[0])
elif n == 2:
    print(wines[0] + wines[1])
else:    
    dp = [0] * (n + 1)
    dp[1] = wines[0]
    dp[2] = wines[0] + wines[1]
    dp[3] = max(wines[0] + wines[1], wines[0] + wines[2], wines[1] + wines[2])

    for i in range(4, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + wines[i-1], dp[i-3] + wines[i-2] + wines[i-1])

    print(dp[n])