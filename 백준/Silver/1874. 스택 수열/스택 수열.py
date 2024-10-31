import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
operations = []
current = 1

is_possible = True
for number in sequence:
    while current <= number:
        stack.append(current)
        operations.append("+")
        current += 1

    if stack[-1] == number:
        stack.pop()
        operations.append("-")
    else:
        is_possible = False

if is_possible:
    for op in operations:
        print(op)
else:
    print("NO")