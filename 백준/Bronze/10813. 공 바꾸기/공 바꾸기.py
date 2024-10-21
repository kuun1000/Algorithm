n, m = tuple(map(int, input().split()))
arr = [i for i in range(n + 1)]

for _ in range(m):
    i, j = tuple(map(int, input().split()))
    arr[j], arr[i] = arr[i], arr[j]
print(*arr[1:])