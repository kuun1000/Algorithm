def get_permutation(seq):
    if len(seq) == n:
        print(*seq)
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            get_permutation(seq+[i])
            visited[i] = False



n = int(input())

seq = []
visited = [False] * (n+1)

get_permutation(seq)