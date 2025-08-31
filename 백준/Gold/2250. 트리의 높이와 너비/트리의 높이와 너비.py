import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def inorder(u, level):
    global counter
    if u == -1:
        return 
    
    inorder(left[u], level+1)

    col = counter
    counter += 1

    if col < min_col[level]:
        min_col[level] = col
    if col > max_col[level]:
        max_col[level] = col

    inorder(right[u], level+1)

# 1. 입력 처리
n = int(input())
left = [-1] * (n+1)
right = [-1] * (n+1)
indeg = [0] * (n+1)

for _ in range(n):
    p, l, r = map(int, input().split())
    left[p] = l
    right[p] = r
    if l != -1:
        indeg[l] += 1
    if r != -1:
        indeg[r] += 1

# 2. 루트 노드 찾기
root = 0
for i in range(1, n+1):
    if indeg[i] == 0:
        root = i
        break

# 3. 중위순회
counter = 1
INF = 10**9
min_col = [INF] * (n+2)
max_col = [0] * (n+2)
inorder(root, 1)

# 4. 레벨별 너비 계산 및 최댓값 찾기
best_level, best_width = 1, 0
level = 1
while level <= n and max_col[level] > 0:
    width = max_col[level] - min_col[level] + 1
    if width > best_width:
        best_width = width
        best_level = level
    level += 1

print(best_level, best_width)