import sys

for _ in range(int(input())):
    a, b = tuple(map(int, sys.stdin.readline().split()))
    print(a + b)