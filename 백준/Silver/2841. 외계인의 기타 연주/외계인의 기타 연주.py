import sys
input = sys.stdin.readline

n, p = tuple(map(int, input().split()))

lines = [[] for _ in range(7)]
moves = 0

for _ in range(n):
    string, fret = map(int, input().split())

    # 현재 줄의 프렛 상태 관리 스택
    stack = lines[string]

    # 현재 프렛보다 높은 프렛들을 모두 뗌
    while stack and stack[-1] > fret:
        stack.pop()
        moves += 1

    # 같은 프렛이 이미 눌려져 있으면 아무것도 안함
    if stack and stack[-1] == fret:
        continue

    # 필요한 프렛을 누름
    stack.append(fret)
    moves += 1

print(moves)