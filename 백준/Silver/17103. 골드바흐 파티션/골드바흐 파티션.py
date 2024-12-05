import math

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(max_num)) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    return is_prime

MAX_NUM = 1000000

prime_list = sieve_of_eratosthenes(MAX_NUM)

t = int(input())
for _ in range(t):
    n = int(input())

    result = 0
    for a in range(2, n // 2 + 1):
        if prime_list[a] and prime_list[n - a]:
            result += 1

    print(result)