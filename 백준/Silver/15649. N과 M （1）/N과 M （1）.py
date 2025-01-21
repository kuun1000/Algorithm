def backtrack(n, m, seq, visited):
    if len(seq) == m:
        print(" ".join(map(str, seq)))
        return 
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            backtrack(n, m, seq + [i], visited)
            visited[i] = False

def solve(n, m):
    visited = [False] * (n + 1)
    backtrack(n, m, [], visited)


n, m = map(int, input().split())
solve(n, m)