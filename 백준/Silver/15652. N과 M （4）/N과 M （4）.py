def backtrack(n, m, seq):
    if len(seq) == m:
        print(*seq)
        return

    for i in range(1, n+1):
        if len(seq) != 0 and seq[-1] > i:
            continue
        backtrack(n, m, seq + [i])

n, m = map(int, input().split())
backtrack(n, m, [])