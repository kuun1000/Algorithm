import sys
input = sys.stdin.readline

n = int(input())
coords = list(map(int, input().split()))

sorted_unique_coords = sorted(set(coords))
coord_map = {coord: index for index, coord in enumerate(sorted_unique_coords)}
result = [coord_map[coord] for coord in coords]

print(*result)