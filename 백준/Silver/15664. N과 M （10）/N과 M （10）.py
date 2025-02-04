def backtrack(start, visited, seq):
    if len(seq) == m:
        print(*seq)
        return

    
    used = set()
    for i in range(start, n):
        if not visited[i] and nums[i] not in used:
            start = i + 1
            visited[i] = True
            used.add(nums[i])
            seq.append(nums[i])
            backtrack(start, visited, seq)
            seq.pop()
            visited[i] = False



n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [False] * n
start = 0
backtrack(start, visited, [])