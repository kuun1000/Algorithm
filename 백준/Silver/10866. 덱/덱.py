import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

result = deque()
for _ in range(n):
    command = input().split()

    if command[0] == 'push_front':
        result.appendleft(command[1])
    elif command[0] == 'push_back':
        result.append(command[1])
    elif command[0] == 'pop_front':
        print(result.popleft() if result else -1)
    elif command[0] == 'pop_back':
        print(result.pop() if result else -1)
    elif command[0] == 'size':
        print(len(result))
    elif command[0] == 'empty':
        print(0 if result else 1)
    elif command[0] == 'front':
        print(result[0] if result else -1)
    else:
        print(result[-1] if result else -1)