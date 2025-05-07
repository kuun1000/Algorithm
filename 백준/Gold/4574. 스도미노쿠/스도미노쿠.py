import sys
sys.setrecursionlimit(10_000)
input = sys.stdin.readline

def to_idx(pos: str):
    return ord(pos[0]) - 65, int(pos[1]) - 1          # 'A1' → (0,0)

def blk(r, c):
    return (r // 3) * 3 + (c // 3)                    # 0‥8 블록 번호

def set_num(r, c, num, put: bool):
    board[r][c] = num if put else 0
    row_used[r][num]   = put
    col_used[c][num]   = put
    blk_used[blk(r,c)][num] = put

def place_domino(a, r1, c1, b, r2, c2, put: bool):
    set_num(r1, c1, a, put)
    set_num(r2, c2, b, put)
    domino_used[a][b] = domino_used[b][a] = put

def can_put(r, c, num):
    return not (row_used[r][num] or col_used[c][num] or blk_used[blk(r,c)][num])

dirs = ((0,1), (1,0))                                # →, ↓

def solve(pos=0):
    if pos == 81:                                     # 완성
        return True
    r, c = divmod(pos, 9)
    if board[r][c]:                                   # 이미 채워진 칸
        return solve(pos + 1)

    for dr, dc in dirs:                               # 인접 두 칸
        nr, nc = r + dr, c + dc
        if nr >= 9 or nc >= 9 or board[nr][nc]:
            continue
        for a in range(1, 10):
            if not can_put(r, c, a):
                continue
            for b in range(1, 10):
                if a == b or domino_used[a][b] or not can_put(nr, nc, b):
                    continue
                place_domino(a, r, c, b, nr, nc, True)
                if solve(pos + 1):
                    return True
                place_domino(a, r, c, b, nr, nc, False)
    return False

puzzle = 1
while True:
    line = input().strip()
    if line == '0' or line == '':
        break
    N = int(line)

    # 상태 배열 초기화
    board       = [[0]*9 for _ in range(9)]
    row_used    = [[False]*10 for _ in range(9)]
    col_used    = [[False]*10 for _ in range(9)]
    blk_used    = [[False]*10 for _ in range(9)]
    domino_used = [[False]*10 for _ in range(10)]

    # 미리 놓여 있는 도미노
    for _ in range(N):
        a, pa, b, pb = input().split()
        a, b = int(a), int(b)
        r1, c1 = to_idx(pa)
        r2, c2 = to_idx(pb)
        place_domino(a, r1, c1, b, r2, c2, True)

    # 1‥9 단독 숫자
    singles = input().split()
    for num in range(1, 10):
        r, c = to_idx(singles[num-1])
        set_num(r, c, num, True)

    solve()                                          # 백트래킹 시작

    print(f'Puzzle {puzzle}')
    for row in board:
        print(''.join(map(str, row)))
    puzzle += 1
