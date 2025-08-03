import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    arr = list(input().rstrip())
    
    total, score = 0, 0
    for result in arr:
        if result == 'O':
            score += 1
            total += score
        else:
            score = 0
    print(total)