def count_factors(n, p):
    cnt = 0
    while n >= p:
        cnt += n // p
        n //= p
    return cnt

def trailing_zeros(n, m):
    if m == 0 or n == m:
        return 0
    
    cnt_2 = count_factors(n, 2) - count_factors(m, 2) - count_factors(n - m, 2)
    cnt_5 = count_factors(n, 5) - count_factors(m, 5) - count_factors(n - m, 5)

    return min(cnt_2, cnt_5)

n, m = map(int, input().split())
print(trailing_zeros(n, m))