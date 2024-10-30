import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
for _ in range(t):
    ps = list(input().strip())
    stack = []
    is_vps = True
    
    for char in ps:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    if stack:
        is_vps = False
    print("YES\n" if is_vps else "NO\n")