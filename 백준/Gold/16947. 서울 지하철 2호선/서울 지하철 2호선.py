from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
n = int(input().strip())
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1. 리프 노드 제거로 순환선 찾기
degree = [0] * (n + 1)
is_cycle = [True] * (n + 1)  # 기본적으로 순환선이라고 가정
q = deque()

for i in range(1, n + 1):
    degree[i] = len(graph[i])
    if degree[i] == 1:
        q.append(i)
        is_cycle[i] = False  # 리프 노드는 순환선이 아니다.

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if is_cycle[nxt]:
            degree[nxt] -= 1
            if degree[nxt] == 1:
                is_cycle[nxt] = False
                q.append(nxt)

# 2. 순환선으로부터의 최단거리 계산 (BFS)
distance = [-1] * (n + 1)
q = deque()

# 순환선에 해당하는 정점들을 시작점으로 설정
for i in range(1, n + 1):
    if is_cycle[i]:
        distance[i] = 0
        q.append(i)

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if distance[nxt] == -1:  # 아직 방문하지 않은 정점이라면
            distance[nxt] = distance[cur] + 1
            q.append(nxt)

# 결과 출력 (1번 정점부터 N번 정점까지의 거리)
print(' '.join(map(str, distance[1:])))