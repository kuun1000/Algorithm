from collections import deque
import sys
input = sys.stdin.readline


def bfs(n, k):
    if n >= k:
        return n - k
    
    max_pos = 2 * k + 1
    visited = [False] * max_pos
    time = [0] * max_pos

    queue = deque([n])
    visited[n] = True

    while queue:
        current = queue.popleft()

        if current == k:
            break

        for next in (current - 1, current + 1, current * 2):
            if 0 <= next < len(visited) and not visited[next]:
                visited[next] = True
                if next == current * 2:
                    time[next] = time[current]
                    queue.appendleft(next)
                else:
                    time[next] = time[current] + 1
                    queue.append(next)

    return time[k]

n, k = map(int, input().split())
time = bfs(n, k)

print(time)