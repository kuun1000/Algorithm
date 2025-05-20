from collections import deque
import sys
input = sys.stdin.readline

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(r1, c1, count):
    queue = deque([(r1, c1, count)])
    visited[r1][c1] = True

    while queue:
        cur_r, cur_c, cnt = queue.popleft()

        if cur_r == r2 and cur_c == c2:
            return cnt

        for dir in directions:
            next_r, next_c = cur_r + dir[0], cur_c + dir[1]
            if is_valid(next_r, next_c) and not visited[next_r][next_c]:
                queue.append((next_r, next_c, cnt+1))
                visited[next_r][next_c] = True
    return -1

n = int(input())
r1, c1, r2, c2 = list(map(int, input().split()))

directions = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
visited = [[False] * n for _ in range(n)]

print(bfs(r1, c1, 0))