n = int(input())  
arr = list(map(int, input().split())) 

dp = [1] * n  
trace = [-1] * n  

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            trace[i] = j

lis_length = max(dp)
idx = dp.index(lis_length)

lis = []
while idx != -1:
    lis.append(arr[idx])
    idx = trace[idx]

lis.reverse()

print(lis_length)
print(*lis)