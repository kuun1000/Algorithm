import sys
input = sys.stdin.readline

n = int(input())

cords = [list(map(int, input().split())) for _ in range(n)]
cords.sort(key=lambda cords: (cords[1], cords[0]))

for x, y in cords:
    print(x, y)