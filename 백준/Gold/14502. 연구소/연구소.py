from collections import deque
import sys
input = sys.stdin.readline


def get_wall_combination(depth, start, combination):
    if depth == 3:
        wall_combinations.append(combination.copy())
        return 
    
    for i in range(start, len(empty_cells)):
        combination.append(i)
        get_wall_combination(depth + 1, i + 1, combination)
        combination.pop()

def deepcopy(array):
    return [row[:] for row in array]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m

def solve(walls):
    grid_copy = deepcopy(grid)

    # 벽 세우기
    for idx in walls:
        r, c = empty_cells[idx]
        grid_copy[r][c] = 1

    # 바이러스 퍼뜨리기
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([*virus_sources])
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny) and grid_copy[nx][ny] == 0:
                grid_copy[nx][ny] = 2
                queue.append((nx, ny))

    infected = sum(row.count(0) for row in grid_copy)
    return infected
    


# 입력 처리
n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

# 지도 정보 저장
empty_cells, virus_sources = [], []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0: # 빈 칸
            empty_cells.append((i, j))
        elif grid[i][j] == 2:   # 바이러스
            virus_sources.append((i, j))

# 벽 세우는 조합 생성
wall_combinations = []
get_wall_combination(0, 0, [])

# 조합별 시뮬레이션 수행
result = 0
for combination in wall_combinations:
    result = max(result, solve(combination))

print(result)