angles = [int(input()) for _ in range(3)]

if sum(angles) != 180:
    print("Error")
elif angles.count(angles[0]) == 3:
    print("Equilateral")
elif len(set(angles)) == 3:
    print("Scalene")
else:
    print("Isosceles")