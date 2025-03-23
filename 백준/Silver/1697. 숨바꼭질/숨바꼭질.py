from collections import deque
import sys
input = sys.stdin.readline



def bfs(n, k):
    if n >= k:
        return n - k
    
    visited = [False] * (2*k + 1)
    time = [0] * (2*k + 1)

    queue = deque([n])
    visited[n] = True

    while queue:
        current = queue.popleft()

        if current == k:
            return time[current]
        
        for next in (current-1, current+1, current*2):
            if 0 <= next < len(visited) and not visited[next]:
                visited[next] = True
                time[next] = time[current] + 1
                queue.append(next)



n, k  = tuple(map(int, input().split()))
print(bfs(n, k))