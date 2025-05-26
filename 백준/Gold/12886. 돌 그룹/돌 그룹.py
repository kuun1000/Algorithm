from collections import deque
import sys
input = sys.stdin.readline

def solve(a, b, c):
    # 기본 조건 확인: 총합이 3의 배수인지
    total = a + b + c
    if total % 3 != 0:
        return 0
    
    # BFS를 위한 초기 설정
    queue = deque()
    visited = set()

    state = tuple(sorted([a, b, c]))
    queue.append(state)
    visited.add(state)

    # BFS 수행
    pairs = [(0, 1), (0, 2), (1, 2)]
    while queue:
        numbers = queue.popleft()

        if numbers[0] == numbers[1] == numbers[2]:
            return 1
        else:
            for i, j in pairs:
                k = 3 - i - j
                
                if numbers[i] != numbers[j]:
                    x = numbers[i]
                    y = numbers[j]
                    if x > y:
                        x, y = y, x

                    nx = x + x
                    ny = y - x
                    new_state = tuple(sorted([nx, ny, numbers[k]]))
                    
                    if new_state not in visited:
                        queue.append(new_state)
                        visited.add(new_state)
    return 0 


# 입력 처리
a, b, c = tuple(map(int, input().split()))

print(solve(a, b, c))