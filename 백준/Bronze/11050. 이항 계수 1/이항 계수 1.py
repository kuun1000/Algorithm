import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))

a, b = 1, 1

for i in range(1, k+1):
    b *= i

for i in range(n, n-k, -1):
    a *= i

print(a // b)