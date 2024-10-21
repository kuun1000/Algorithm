x = int(input())

result = 0
for _ in range(int(input())):
    a, b = tuple(map(int, input().split()))
    result += a * b

print("Yes" if x == result else "No")