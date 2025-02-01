def backtrack(start, path):
    if len(path) == m:
        print(*path)
        return

    for i in range(start, n):
        backtrack(i+1, path+[nums[i]])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

backtrack(0, [])