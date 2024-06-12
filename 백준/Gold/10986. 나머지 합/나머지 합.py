import sys
input = sys.stdin.readline

n, m  = map(int, input().split())

# 원본 리스트
A = list(map(int, input().split()))

S = [0] * n # 합 배열
C = [0] * m # M으로 나누었을 때 나머지가 같은 원소들의 개수 배열
ans = 0

# 합 배열 계산
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

# C 배열 계산
for i in range(n):
    remainder = S[i] % m
    if remainder == 0: 
        ans += 1
    C[remainder] += 1

# 나머지가 같은 원소의 개수에 대해 2가지를 뽑는 경우의 수
for i in range(m):
    ans += (C[i] * (C[i] - 1)) // 2

print(ans)