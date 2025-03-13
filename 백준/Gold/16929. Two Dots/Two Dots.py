import sys
input = sys.stdin.readline

def solve(grid, n, m):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y, px, py, color, count):
        visited[x][y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if grid[nx][ny] != color:
                continue

            if (nx, ny) == (px, py):
                continue

            if visited[nx][ny]:
                if count >= 4:
                    return True
                continue

            if dfs(nx, ny, x, y, color, count + 1):
                return True
            
        return False

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if dfs(i, j, -1, -1, grid[i][j], 1):
                    return "Yes"
    return "No"    



n, m = tuple(map(int, input().split()))
grid = [list(input().strip()) for _ in range(n)]

print(solve(grid, n, m))