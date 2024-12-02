from math import gcd
from itertools import combinations
    
for _ in range(int(input())):
    n, *arr = map(int, input().split())

    result = 0
    for a, b in combinations(arr, 2):
        result += gcd(a, b)
    print(result)