def backtrack(seq):
    if len(seq) == m:
        print(*seq)
        return
    
    for i in range(n):
        backtrack(seq + [nums[i]])



n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

backtrack([])