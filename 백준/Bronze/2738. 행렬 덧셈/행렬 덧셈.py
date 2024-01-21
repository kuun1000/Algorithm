n, m = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

result = []
for i in range(n):
    result.append(list(map(lambda x, y: x + y, a[i], b[i])))

for i in range(n):
    print(*result[i])