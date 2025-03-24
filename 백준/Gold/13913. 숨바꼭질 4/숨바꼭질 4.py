from collections import deque
import sys
input = sys.stdin.readline



def bfs(n, k):
    if n >= k:
        return n - k, list(range(n, k-1, -1))
    
    max_pos = 2*k + 1
    visited = [False] * max_pos
    time = [0] * max_pos
    prev = [-1] * max_pos

    queue = deque([n])
    visited[n] = True

    while queue:
        current = queue.popleft()

        if current == k:
            break
        
        for next in (current-1, current+1, current*2):
            if 0 <= next < len(visited) and not visited[next]:
                visited[next] = True
                time[next] = time[current] + 1
                prev[next] = current
                queue.append(next)

    path = []
    pos = k
    while pos != -1:
        path.append(pos)
        pos = prev[pos]
    path.reverse()

    return time[k], path



n, k  = tuple(map(int, input().split()))
time, path = bfs(n, k)

print(time)
print(" ".join(map(str, path)))