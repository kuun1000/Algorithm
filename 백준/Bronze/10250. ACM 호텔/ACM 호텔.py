import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = list(map(int, input().split()))
    
    if n % h == 0:
        floor = h
        room = n // h
    else:
        floor = n % h
        room = n // h + 1 

    print(f"{floor}{room:02d}")