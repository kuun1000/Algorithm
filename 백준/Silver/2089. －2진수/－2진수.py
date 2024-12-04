def neg_bin(n):
    if n == 0:
        return "0"

    result = []
    while n != 0:
        remainder = n % -2
        n //= -2

        if remainder < 0:
            remainder += 2
            n += 1
        result.append(str(remainder))
    return ''.join(result[::-1])


n = int(input())
print(neg_bin(n))