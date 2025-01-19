tets = [
    [(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)], 
    [(0,1), (1,0), (1,1)],
    [(1,0),(1,1),(2,1)], [(0,-1), (1,-1), (1,-2)],
    [(1,0), (1,-1), (2,-1)], [(0,1), (1,1), (1,2)],
    [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)], 
    [(0,1),(1,1), (2,1)], [(0,1), (0,2), (-1,2)],
    [(1,0),(2,0),(2,-1)], [(0,1),(0,2),(1,2)], 
    [(1,0),(2,0),(0,1)], [(1,0),(1,1),(1,2)],
    [(1,0),(1,1),(1,-1)], [(1,0),(1,1),(2,0)], 
    [(0,-1),(1,0),(0,1)], [(0,1),(-1,1),(1,1)] 
]    

def check(i, j, tet):
    temp = arr[i][j]
    for di, dj in tet:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            temp += arr[ni][nj]
        else:
            return 0
    return temp

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        for tet in tets:
            temp = check(i, j, tet)
            ans = max(temp, ans)

print(ans)