import sys
input = sys.stdin.readline

def dfs(sequence, current_sum):
    if len(sequence) == 2:
        return current_sum
    
    result = 0
    for i in range(1, len(sequence) - 1):
        energy = sequence[i-1] * sequence[i+1]
        removed = sequence.pop(i)
        result = max(result, dfs(sequence, current_sum + energy))
        sequence.insert(i, removed)
    return result


n = int(input())
weights = list(map(int, input().split()))

max_sum = dfs(weights, 0)
print(max_sum)