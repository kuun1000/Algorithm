def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)    

for _ in range(int(input())):
    a, b = tuple(map(int, input().split()))
    print(lcm(a, b))