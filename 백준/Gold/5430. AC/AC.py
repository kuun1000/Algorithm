from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    arr = input().strip()

    # 배열 파싱
    if n == 0:
        queue = deque()
    else:
        queue = deque(map(int, arr[1:-1].split(',')))

    reverse = False
    error = False

    for cmd in p:
        if cmd == 'R':
            reverse = not reverse
        elif cmd == 'D':
            if not queue:
                error = True
                break
            if reverse:
                queue.pop()
            else:
                queue.popleft()

    if error:
        print('error')
    else:
        if reverse:
            queue.reverse()
        print('[' + ','.join(map(str, queue)) + ']')