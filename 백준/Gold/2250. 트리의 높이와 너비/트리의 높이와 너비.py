import sys
input = sys.stdin.readline

def inorder(node, depth):
    global col 
    if node == -1:
        return
    
    # 왼쪽 자식 방문
    inorder(tree[node][0], depth + 1)

    # 현재 노드 방문
    if depth not in level_min:
        level_min[depth] = col
    else:
        level_min[depth] = min(level_min[depth], col)

    if depth not in level_max:
        level_max[depth] = col
    else:
        level_max[depth] = max(level_max[depth], col)
    
    col += 1    # 열 번호 증가

    # 오른쪽 자식 방문
    inorder(tree[node][1], depth + 1)



# 1. 입력 처리
n = int(input())
tree = {}
is_child = [False] * (n + 1)

for _ in range (1, n + 1):
    node, left, right = map(int, input().split())
    tree[node] = [left, right]
    if left != -1:
        is_child[left] = True
    if right != -1:
        is_child[right] = True

# 2. 루트 노드 찾기
root = None
for i in range(1, n + 1):
    if not is_child[i]:
        root = i
        break

# 중위 순회
level_min, level_max = {}, {}
col = 1
inorder(root, 1)

# 각 레벨별 너비 계산 및 최대 너비 계산
max_width = 0
result_level = 0
max_depth = max(level_max.keys())

for depth in range(1, max_depth + 1):
    width = level_max[depth] - level_min[depth] + 1
    if width > max_width:
        max_width = width
        result_level = depth

print(result_level, max_width)