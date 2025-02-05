def backtrack(seq):
    if len(seq) == m:
        print(*seq)
        return
    
    prev = -1

    for i in range(n):
        if nums[i] == prev:
            continue
        prev = nums[i]
        backtrack(seq + [nums[i]])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
backtrack([])