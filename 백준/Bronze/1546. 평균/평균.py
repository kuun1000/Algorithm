n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)
result = [(i / max_val * 100) for i in arr]
print(sum(result) / n)