# 변수 선언 및 입력
n, b = input().split()
length = len(n) # 자릿수
b = int(b)

# b진법 수 중 알파벳 문자를 숫자로 변환
digits = [0] * length   # b진법 수 
for i in range(length):
    if 'A' <= n[i] <= 'Z':
        digits[i] = ord(n[i]) - 55
    else:
        digits[i] = int(n[i])

number = 0  # 10진수로 변환된 수 
if b == 10: # 10진법으로 바꾸는 경우
    number = n  # 그대로 출력

else:   # 10진법 이외의 진법으로 바꾸는 경우
    for i in range(length): # 각 자리수에 대해 
        # 해당 자릿수의 값 X (진법의 제곱근)
        number += (digits[i] * (b ** (length - i - 1))) 

print(number)