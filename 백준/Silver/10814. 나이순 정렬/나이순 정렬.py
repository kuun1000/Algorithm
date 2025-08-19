import sys
input = sys.stdin.readline

n = int(input())
arr = [[int(age), name, i] for i, (age, name) in enumerate(input().split() for _ in range(n))]

arr.sort(key=lambda x: (x[0], x[2]))

for elem in arr:
    print(elem[0], elem[1])