import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    sentance = list(input().split())
    stack = []
    for word in sentance:
        stack.append(word[::-1])
    print(*stack)