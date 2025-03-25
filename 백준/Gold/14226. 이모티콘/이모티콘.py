from collections import deque
import sys
input = sys.stdin.readline



def bfs(s):
    max_val = 2 * s
    visited = [[False] * (max_val + 1) for _ in range(max_val + 1)]

    queue = deque()
    queue.append((1, 0, 0))
    visited[1][0] = True

    while queue:
        screen, clipboard, time = queue.popleft()

        if screen == s:
            return time
        
        # 화면의 이모티콘을 모두 복사해서 클립보드에 저장하기
        if not visited[screen][screen]:
            visited[screen][screen] = True
            queue.append((screen, screen, time + 1))

        # 클립보드에 있는 이모티콘을 화면에 붙여넣기
        if clipboard > 0 and screen + clipboard <= max_val and not visited[screen + clipboard][clipboard]:
            visited[screen + clipboard][clipboard] = True
            queue.append((screen+clipboard, clipboard, time + 1))
        
        # 화면에 있는 이모티콘 중 하나 삭제하기
        if screen > 0 and not visited[screen - 1][clipboard]:
            visited[screen - 1][clipboard] = True
            queue.append((screen - 1, clipboard, time + 1))

s = int(input())
print(bfs(s))