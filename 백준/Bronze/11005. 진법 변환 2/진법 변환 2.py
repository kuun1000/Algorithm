n, b = map(int, input().split())

ans = ''
while n > 0:
    remain = n % b  # n을 b로 나눈 나머지를 계산
    if remain >= 10:
        ans = chr(ord('A') + (remain - 10)) + ans  # 10 이상일 때 A~Z로 변환
    else:
        ans = str(remain) + ans  # 10 미만일 때 숫자를 그대로 추가
    n //= b  # n을 b로 나눔

print(ans)