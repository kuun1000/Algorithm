import sys
input = sys.stdin.readline

arr = input().strip()
stack = []
result = 0

for i in range(len(arr)):
    if arr[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if arr[i - 1] == "(":
            result += len(stack)
        else:
            result += 1

print(result)