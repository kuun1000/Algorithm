from collections import deque
import sys
input = sys.stdin.readline


# 이동 함수
def get_final_pos(pos):
    # 사다리 시작 칸인 경우
    if pos in ladders.keys():
        final_pos = ladders[pos]
    # 뱀의 머리 칸인 경우
    elif pos in snakes.keys():
        final_pos = snakes[pos]
    # 기본 칸인 경우
    else:
        final_pos = pos
    return final_pos

def bfs(position, roll_count):

    queue = deque([[position, roll_count]])
    visited[position] = True

    while queue:
        pos, cnt = queue.popleft()

        if pos == 100:
            return cnt

        for d in range(1, 7):
            if pos + d > 100:
                continue
            next_pos = get_final_pos(pos + d)
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append([next_pos, cnt + 1])

# 입력 처리
n, m = tuple(map(int, input().split()))

ladders = {}
for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

snakes = {}
for _ in range(m):
    x, y = map(int, input().split())
    snakes[x] = y

visited = [False] * 101
print(bfs(1, 0))