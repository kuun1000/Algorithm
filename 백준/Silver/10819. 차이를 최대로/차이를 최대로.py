def get_sum(seq):
    result = 0
    for i in range(n-1):
        result += abs(seq[i] - seq[i+1])
    return result

def get_permutation(seq):
    global max_sum
    if len(seq) == n:
        max_sum = max(max_sum, get_sum(seq))
        return 

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            get_permutation(seq+[arr[i]])
            visited[i] = False
    


n = int(input())
arr = list(map(int, input().split()))

visited = [False] * (n)
max_sum = 0
get_permutation([])

print(max_sum)