import sys
input = sys.stdin.readline
import math

n = int(input())
sizes = list(map(int, input().split()))
t, p = list(map(int, input().split()))

tshirt, pen = 0, 0

for size in sizes:
    tshirt += math.ceil(size/t)


print(tshirt)
print(n // p, n % p)