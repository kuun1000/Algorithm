import sys
import math

# 에라토스테네스의 체로 소수 리스트 생성
def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(max_num)) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    return is_prime

# 최대 범위 설정
MAX_NUM = 1000000
prime_list = sieve_of_eratosthenes(MAX_NUM)

# 소수만 추출 (홀수 소수 리스트)
prime_numbers = [i for i in range(3, MAX_NUM + 1, 2) if prime_list[i]]

# 입력 처리
input_data = sys.stdin.read().strip().split()
results = []

# 각 짝수 n에 대해 골드바흐의 추측 확인
for line in input_data:
    n = int(line)
    if n == 0:
        break
    
    found = False
    for a in prime_numbers:
        if a > n // 2:  # 대칭성을 이용해 절반까지만 확인
            break
        b = n - a
        if prime_list[b]:
            results.append(f"{n} = {a} + {b}")
            found = True
            break
    
    if not found:
        results.append("Goldbach's conjecture is wrong.")

# 결과 출력
sys.stdout.write("\n".join(results) + "\n")