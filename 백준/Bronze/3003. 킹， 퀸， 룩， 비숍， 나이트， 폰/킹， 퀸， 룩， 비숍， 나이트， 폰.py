correct = [1, 1, 2, 2, 2, 8]
current = list(map(int, input().split()))

print(*[x - y for x, y in zip(correct, current)])