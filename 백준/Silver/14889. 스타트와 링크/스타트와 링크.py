import sys

def dfs(idx, count):
    global min_diff

    if count == N // 2:
        start_team = [i for i in range(N) if selected[i]]
        link_team = [i for i in range(N) if not selected[i]]
        
        start_score, link_score = 0, 0
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                start_score += S[start_team[i]][start_team[j]] + S[start_team[j]][start_team[i]]
                link_score += S[link_team[i]][link_team[j]] + S[link_team[j]][link_team[i]]
                
        diff = abs(start_score - link_score)
        if diff == 0:
            print(0)
            sys.exit(0)
        min_diff = min(min_diff, diff)
        return

    for i in range(idx, N):
        if not selected[i]:
            selected[i] = True
            dfs(i + 1, count + 1)
            selected[i] = False

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
min_diff = sys.maxsize
selected = [False] * N
selected[0] = True  
dfs(1, 1)
print(min_diff)