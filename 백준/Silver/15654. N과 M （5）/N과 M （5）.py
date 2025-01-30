def backtrack():
    if len(result) == m:
        print(*result)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(nums[i])
            backtrack()
            result.pop()
            visited[i] = False

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [False] * (n)
result = []

backtrack()