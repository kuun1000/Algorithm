def backtrack(n, m, nums, visited, seq):
    if len(seq) == m:
        print(*seq)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            backtrack(n, m, nums, visited, seq + [nums[i]])
            visited[i] = False

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * (n)
backtrack(n, m, nums, visited, [])