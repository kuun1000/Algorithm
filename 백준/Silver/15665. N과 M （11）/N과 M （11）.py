def backtrack(seq):
    if len(seq) == m:
        print(*seq)
        return
    
    used = set()

    for i in range(n):
        if nums[i] in used:
            continue
        used.add(nums[i])
        backtrack(seq + [nums[i]])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
backtrack([])