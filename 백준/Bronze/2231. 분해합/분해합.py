n = int(input())

constructor = n
for i in range(n-1, 1, -1):
    digits = list(map(int, str(i)))
    if n == (i + sum(digits)):
        constructor = min(constructor, i)
if constructor == n:
    print(0)
else:
    print(constructor)