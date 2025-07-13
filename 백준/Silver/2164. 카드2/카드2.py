from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
cards = deque(list(range(1, n+1)))

while len(cards) > 1:
    cards.popleft()
    front = cards.popleft()
    cards.append(front)

print(cards.popleft())