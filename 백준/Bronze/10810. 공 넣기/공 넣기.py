n, m = tuple(map(int, input().split()))
arr = [0] * (n + 1)

for _ in range(m):
    i, j, k = tuple(map(int, input().split()))
    arr[i:j+1] = [k] * (j - i + 1)
print(*arr[1:])