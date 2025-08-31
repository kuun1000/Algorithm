import sys
input = sys.stdin.readline

def traverse(node, order):
    if node == '.':
        return ""
    
    result = ""
    for char in order:
        if char == 'N':
            result += node
        elif char == 'L':
            result += traverse(tree[node][0], order)
        elif char == 'R':
            result += traverse(tree[node][1], order)
    return result

tree = {}
n = int(input())
for _ in range(n):
    node, left, right = input().split()
    tree[node] = (left, right)

print(traverse('A', 'NLR')) # 전위 순회
print(traverse('A', 'LNR')) # 중위 순회
print(traverse('A', 'LRN')) # 후위 순회