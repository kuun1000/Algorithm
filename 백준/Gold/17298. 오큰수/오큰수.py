import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
ans = [0] * n
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:   # 오큰수 조건
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

print(*ans)