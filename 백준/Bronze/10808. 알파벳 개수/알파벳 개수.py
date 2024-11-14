import sys
input = sys.stdin.readline

s = list(input().strip())

stack = [0] * 26

for letter in s:
    stack[ord(letter) - ord('a')] += 1

print(*stack)