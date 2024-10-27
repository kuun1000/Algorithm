import math

a, b, v = tuple(map(int, input().split()))
print(math.ceil((v - b) / (a - b)))