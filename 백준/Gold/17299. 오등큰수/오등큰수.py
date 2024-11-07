import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

frequency = {}
for num in arr:
    frequency[num] = frequency.get(num, 0) + 1 

result = [-1] * n
stack = []

for i in range(n):
    while stack and frequency[arr[stack[-1]]] <frequency[arr[i]]:
        index = stack.pop()
        result[index] = arr[i]
    stack.append(i)

print(*result)