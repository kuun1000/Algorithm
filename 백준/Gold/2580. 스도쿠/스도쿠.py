import sys
input = sys.stdin.readline

# 행, 열, 박스 체크를 위한 집합
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]

grid = []
empty_cells = []

# 입력과 동시에 사용된 숫자 추적
for i in range(9):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(9):
        num = row[j]
        if num == 0:
            empty_cells.append((i, j))
        else:
            rows[i].add(num)
            cols[j].add(num)
            boxes[(i // 3) * 3 + j // 3].add(num)

def solve(idx):
    if idx == len(empty_cells):
        for row in grid:
            print(' '.join(map(str, row)))
        return True

    x, y = empty_cells[idx]
    box_idx = (x // 3) * 3 + y // 3

    for num in range(1, 10):
        if num not in rows[x] and num not in cols[y] and num not in boxes[box_idx]:
            grid[x][y] = num
            rows[x].add(num)
            cols[y].add(num)
            boxes[box_idx].add(num)

            if solve(idx + 1):
                return True

            # 백트래킹
            grid[x][y] = 0
            rows[x].remove(num)
            cols[y].remove(num)
            boxes[box_idx].remove(num)

    return False

solve(0)