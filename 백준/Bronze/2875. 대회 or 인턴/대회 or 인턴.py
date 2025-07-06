import sys
input = sys.stdin.readline


n, m, k = list(map(int, input().split()))

females = list(range(2, n+1, 2))
males = list(range(1, m+1))

team = 0
current = 0
remain = n + m
for f, m in zip(females, males):
    current += 3
    remain -= 3
    if remain < k:
        break
    
    team += 1

print(team)