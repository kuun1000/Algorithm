def count_factors(n, p):
    count = 0
    while n >= p:
        count += n // p
        n //= p
    return count

def trailing_zeros_in_combination(n, m):
    if m == 0 or n == m:
        return 0

    count_2 = count_factors(n, 2) - count_factors(m, 2) - count_factors(n - m, 2)
    count_5 = count_factors(n, 5) - count_factors(m, 5) - count_factors(n - m, 5)
    
    return min(count_2, count_5)

n, m = map(int, input().split())
print(trailing_zeros_in_combination(n, m))