from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline



def bfs(node, graph, color):
    queue = deque([node])
    while queue:
        current = queue.popleft()
        next_color = color[current] % 2 + 1

        for next in graph[current]:
            if not color[next]:
                color[next] = next_color
                queue.append(next)
            elif color[next] != next_color:
                return False
    return True

def solve():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    color = [0] * (v + 1)
    for i in range(1, v + 1):
        if color[i]:
            continue
        color[i] = 1

        if bfs(i, graph, color) == False:
            return "NO"    
    return "YES"



k = int(input())
for testcase in range(k):
    print(solve())