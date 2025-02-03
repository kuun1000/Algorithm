def backtrack(visited, seq):
    if len(seq) == m:
        print(*seq)
        return

    used = set()
    for i in range(n):
        if not visited[i] and nums[i] not in used:
            visited[i] = True
            used.add(nums[i])
            backtrack(visited, seq + [nums[i]])
            visited[i] = False



n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [False] * n
backtrack(visited, [])