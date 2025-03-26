from collections import deque
import sys
input = sys.stdin.readline


def bfs(n, k):
    if n >= k:
        return n - k
    
    max_pos = 2 * k + 1
    time = [-1] * max_pos

    queue = deque([n])
    time[n] = 0
    
    while queue:
        current = queue.popleft()

        if current == k:
            return time[k]

        for next in (current - 1, current + 1, current * 2):
            if 0 <= next < len(time) and time[next] == -1:
                if next == current * 2:
                    time[next] = time[current]
                    queue.appendleft(next)
                else:
                    time[next] = time[current] + 1
                    queue.append(next)


n, k = map(int, input().split())
time = bfs(n, k)

print(time)