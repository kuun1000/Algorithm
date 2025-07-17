from collections import deque

def solution(priorities, location):
    queue = deque((p, i) for i, p in enumerate(priorities))
    cnt = 0

    while queue:
        priority, idx = queue.popleft()

        if any(p > priority for p, _ in queue):
            queue.append((priority, idx))
        else:
            cnt += 1
            if idx == location:
                return cnt