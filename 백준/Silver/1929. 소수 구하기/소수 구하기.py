import math

m, n = tuple(map(int, input().split()))

array = [True] * (n + 1)
array[0] = array[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        for j in range(i * i, n + 1, i):
            array[j] = False

result = [i for i in range(m, n + 1) if array[i]]
print("\n".join(map(str, result)))