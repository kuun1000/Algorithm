n = int(input())
numbers = list(map(int, input()))

result = 0
for i in range(n):
    result += numbers[i]

print(result)