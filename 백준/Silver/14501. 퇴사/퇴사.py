def best_profit(date, total):
    global max_profit

    if date >= n:
        max_profit = max(max_profit, total)
        return
    
    if date + schedule[date][0] <= n:
        best_profit(date+schedule[date][0], total+schedule[date][1])
    
    best_profit(date+1, total)



n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

max_profit = 0
best_profit(0, 0)
print(max_profit)