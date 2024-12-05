import math

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아니므로 False로 설정
    
    for i in range(2, int(math.sqrt(max_num)) + 1):
        if is_prime[i]:  # i가 소수인 경우
            # i의 배수들은 소수가 아니므로 False로 설정
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    return is_prime, [i for i in range(2, max_num + 1) if is_prime[i]]

MAX_NUM = 1000000 

prime_list, primes = sieve_of_eratosthenes(MAX_NUM)

t = int(input())
for _ in range(t):
    n = int(input()) 

    result = 0
    # 소수 리스트에서 n/2 이하의 소수만 순회
    for p in primes:
        if p > n // 2:
            break
        if prime_list[n - p]:   # n-p가 소수인지 확인
            result += 1  # 파티션 개수 증가

    print(result)