def find_year(e, s, m):
    e -= 1
    s -= 1
    m -= 1

    year = e
    while True:
        if (year % 28 == s) and (year % 19 == m):
            return year + 1
        year += 15 

e, s, m = map(int, input().split())
print(find_year(e, s, m))