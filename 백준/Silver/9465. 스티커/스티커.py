t = int(input())

for _ in range(t):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue

    dp = [[0] * 2 for _ in range(n+1)]
    dp[1] = [stickers[0][0], stickers[1][0]]

    for i in range(2, n+1):
        dp[i][0] = max(dp[i-1][1], dp[i-2][1]) + stickers[0][i-1]
        dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + stickers[1][i-1]

    print(max(dp[n][0], dp[n][1]))