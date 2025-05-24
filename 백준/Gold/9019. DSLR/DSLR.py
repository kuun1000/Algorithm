from collections import deque
import sys
input = sys.stdin.readline

def D(n):
    return (n * 2) % 10000

def S(n):
    return 9999 if n == 0 else n - 1

def L(n):
    s = str(n).zfill(4)
    return int(s[1:] + s[0])

def R(n):
    s = str(n).zfill(4)
    return int(s[-1] + s[:-1])

def bfs(number):
    queue = deque([(number, "")])
    visited[number] = True

    while queue:
        num, comm = queue.popleft()

        if num == b:
            return comm
        
        for func, c in [(D, 'D'), (S, 'S'), (L, 'L'), (R, 'R')]:
            result = func(num)
            if not visited[result]:
                visited[result] = True
                queue.append((result, comm + c))

t = int(input())
for _ in range(t):
    a, b = tuple(map(int, input().split()))

    visited = [False] * 10000
    print(bfs(a))