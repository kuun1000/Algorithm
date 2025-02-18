import sys

def calculate_ability(team):
    ability = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            ability += abilities[team[i]][team[j]] + abilities[team[j]][team[i]]
    return ability

def minimum_ability(index, count):
    global min_ability

    if count == n // 2:
        start_team = []
        link_team = []

        for i in range(n):
            if visited[i]:
                start_team.append(i)
            else:
                link_team.append(i)
        
        start_ability = calculate_ability(start_team)
        link_ability = calculate_ability(link_team)

        min_ability = min(min_ability, abs(start_ability - link_ability))

    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            minimum_ability(i+1, count+1)
            visited[i] = False



n = int(input())
abilities = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
min_ability = sys.maxsize

minimum_ability(0, 0)
print(min_ability)