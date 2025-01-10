def tile_count(n):
    if n % 2 != 0:
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1  
    dp[2] = 3  

    
    for i in range(4, n + 1, 2): 
        dp[i] = dp[i - 2] * 3  
        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2

    return dp[n]


n = int(input())
print(tile_count(n))