sides = list(map(int, input().split()))

sides = sorted(sides, reverse=True)
if sides[0] >= sides[1] + sides[2]:
    sides[0] = sides[1] + sides[2] - 1

print(sum(sides))