from itertools import combinations

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a %b)
    
for _ in range(int(input())):
    n, *arr = map(int, input().split())
    combi = list(combinations(arr, 2))

    result = 0
    for a, b in combi:
        result += gcd(a, b)
    print(result)