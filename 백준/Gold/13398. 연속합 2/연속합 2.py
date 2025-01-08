n = int(input())
arr = list(map(int, input().split()))


left_dp = [0] * n
left_dp[0] = arr[0]

for i in range(1, n):
    left_dp[i] = max(arr[i], left_dp[i-1] + arr[i])


right_dp = [0] * n
right_dp[n-1] = arr[n-1]

for i in range(n-2, -1, -1):
    right_dp[i] = max(arr[i], right_dp[i+1] + arr[i])


max_sum = max(left_dp)

for i in range(1, n-1):
    max_sum = max(max_sum, left_dp[i-1] + right_dp[i+1])

print(max_sum)