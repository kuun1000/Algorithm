def count_digits(n):
    length = 0
    digit = 1
    start = 1

    while start <= n:
        end = min(n, start * 10 - 1)
        count = end - start + 1
        length += count * digit

        start *= 10
        digit += 1

    return length

n = int(input())
print(count_digits(n))