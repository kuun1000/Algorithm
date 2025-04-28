import sys
input = sys.stdin.readline

def dfs(sequence, current_sum):
    global max_sum
    if len(sequence) == 2:
        max_sum = max(max_sum, current_sum)
    
    for i in range(1, len(sequence) - 1):
        dfs(sequence[:i]+sequence[i+1:], current_sum + sequence[i-1] * sequence[i+1]) 


n = int(input())
weights = list(map(int, input().split()))

max_sum = 0 
dfs(weights, 0)

print(max_sum)