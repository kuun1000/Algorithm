from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    if s == t:
        return '0'

    while queue:
        x, path = queue.popleft()

        if x == t:
            return path
        
        y = None
        for op in ['*', '+', '-', '/']:
            if op == '*':
                y = x * x
            elif op == '+':
                y = x + x
            elif op == '-':
                y = 0
            elif op == '/' and x != 0:
                y = 1

            if y is not None and y > t:
                continue    

            if y is not None and y not in visited:
                visited.add(y)
                queue.append((y, path+op))
    
    return '-1'

# 입력 처리
s, t = map(int, input().split())

# 초기화
queue = deque([(s, "")])
visited = set()
visited.add(s)

# BFS 
print(bfs())