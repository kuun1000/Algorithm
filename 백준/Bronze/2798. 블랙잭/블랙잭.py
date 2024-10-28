n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum_val = cards[i] + cards[j] + cards[k]
            if sum_val <= m:
                max_sum = max(max_sum, sum_val)
                
print(max_sum)