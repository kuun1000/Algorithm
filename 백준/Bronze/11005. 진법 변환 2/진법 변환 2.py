import sys

# 변수 입력 및 선언
n, b = tuple(map(int, sys.stdin.readline().split()))
digits = []

# 10진법 -> N진법 변환
while True:
    if n < b:
        digits.append(n)
        break
    digits.append(n % b)
    n //= b

# 10진법 넘어가는 진법인 경우, 알파벳 대문자 사용
for digit in digits[::-1]:
    if 10 <= digit <= 35:
        print(chr(digit + 55), end="")
    else:
        print(digit, end="")