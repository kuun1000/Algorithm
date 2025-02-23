def sovle():
    cnt = 0
    for bitmask in range(1, 1 << n):
        subset = []

        for i in range(n):
            if bitmask & (1 << i):
                subset.append(arr[i])
    
        if sum(subset) == s:
            cnt += 1
    return cnt

n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = sovle()
print(cnt)