x, y = [0] * 3, [0] * 3
for i in range(3):
    x[i], y[i] = map(int, input().split())

print(min(x, key=x.count), min(y, key=y.count))