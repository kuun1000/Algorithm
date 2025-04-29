import sys
input = sys.stdin.readline

def dfs(row):
    
    if row == n:
        return 1
    
    total = 0
    for col in range(n):
        if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
            total += dfs(row+1)
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False
    return total
    


n = int(input())
cols = [False] * n 
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)

print(dfs(0))