A = int(input())
B = input()
results = []

for i in range(2, -1, -1):
    result = A * int(B[i])
    results.append(result * (10 ** (2 - i)))
    print(result)
print(sum(results))