import sys
input = sys.stdin.readline

n = int(input())

cords = [list(map(int, input().split())) for _ in range(n)]
cords.sort(key=lambda cords: (cords[0], cords[1]))

for x, y in cords:
    print(x, y)