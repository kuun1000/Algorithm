def backtrack(start, seq):
    if len(seq) == m:
        print(*seq)
        return

    for i in range(start, n):
        if i > start and nums[i] == nums[i - 1]:
            continue
        backtrack(i + 1, seq + [nums[i]])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
backtrack(0, [])
