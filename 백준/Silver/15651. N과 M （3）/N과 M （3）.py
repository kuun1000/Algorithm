def product(nums, n, m):
    def backtrack(path):
        if len(path) == m:
            print(*path)
            return

        for i in range(n):
            path.append(nums[i])
            backtrack(path)
            path.pop()
    
    backtrack([])

n, m = map(int, input().split())
nums = list(range(1, n+1))
product(nums, n, m)