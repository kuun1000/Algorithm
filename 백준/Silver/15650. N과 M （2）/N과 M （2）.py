def backtrack(start, path, n, m):
    if len(path) == m:
        print(" ".join(map(str, path)))
        return
    
    for i in range(start, n + 1):
        backtrack(i + 1, path + [i], n, m)

n, m = map(int, input().split())
backtrack(1, [], n, m)