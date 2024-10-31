import sys
input = sys.stdin.readline

left_stack = list(input().strip())
right_stack = []

m = int(input())

for _ in range(m):
    command = input().split()
    if command[0] == 'L':  
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':  
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':  
        if left_stack:
            left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])

print(''.join(left_stack + right_stack[::-1]))