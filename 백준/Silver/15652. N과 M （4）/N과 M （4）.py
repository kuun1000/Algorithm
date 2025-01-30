def backtrack(n, m, seq):
    if len(seq) == m:
        print(*seq)
        return

    start = seq[-1] if seq else 1

    for i in range(start, n+1):
        backtrack(n, m, seq + [i])

n, m = map(int, input().split())
backtrack(n, m, [])