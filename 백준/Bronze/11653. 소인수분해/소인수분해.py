import math

def isPrime(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return is_prime

def prime_factorization(n):
    limit = int(math.sqrt(n)) + 1
    prime_list = isPrime(limit)

    for i in range(2, len(prime_list)):
        if prime_list[i]:
            while n % i == 0:
                print(i)
                n //= i

    if n > 1:
        print(n)

n = int(input())
if n > 1:
    prime_factorization(n)