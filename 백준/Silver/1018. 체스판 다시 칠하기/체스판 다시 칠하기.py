m, n = map(int, input().split())
board = [list(input()) for _ in range(m)]

pattern_w = [['W' if (i+j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)]
pattern_b = [['B' if (i+j) % 2 == 0 else 'W' for j in range(8)] for i in range(8)]

repaints = []
for i in range(m - 7):
    for j in range(n - 7):
        chessboard = [row[j:j+8] for row in board[i:i+8]]
        
        repaint_w = 0
        repaint_b = 0
        for a in range(8):
            for b in range(8):
                if chessboard[a][b] != pattern_w[a][b]:
                    repaint_w += 1
                if chessboard[a][b] != pattern_b[a][b]:
                    repaint_b += 1
        repaints.append(min(repaint_w, repaint_b))

print(min(repaints))