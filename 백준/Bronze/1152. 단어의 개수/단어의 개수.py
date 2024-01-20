# 앞뒤 공백 제거
s = input().strip()

if len(s) == 0:
    print(0)
else:
    # 공백 기준 분리
    s = list(s.split(" "))
    print(len(s))
