import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = [-1] * n
stack = []

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        index = stack.pop()
        result[index] = arr[i]
    stack.append(i)

print(*result)