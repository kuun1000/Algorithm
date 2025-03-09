from collections import deque
import sys
input = sys.stdin.readline

def in_bound(x, y, length):
    return 0 <= x < length and 0 <= y < length

def bfs(length, visited, current, target):
    cx, cy = current
    tx, ty = target

    queue = deque([(cx, cy, 0)])
    visited[cx][cy] = True

    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                  (-2, 1), (-1, 2), (1, 2), (2, 1)]
    
    while queue:
        cx, cy, cnt = queue.popleft()

        if cx == tx and cy == ty:
            return cnt

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if in_bound(nx, ny, length) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))
    return 0



def solve():
    length = int(input())
    current = tuple(map(int, input().split()))
    target = tuple(map(int, input().split()))
    
    visited = [[False] * length for _ in range(length)]

    print(bfs(length, visited, current, target))


k = int(input())
for testcase in range(k):
    solve()