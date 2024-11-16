import sys

# 입력 데이터 읽기
lines = sys.stdin.read().splitlines()

# 각 줄에 대해 처리
for line in lines:
    lower_count = sum(1 for char in line if char.islower())  # 소문자 개수
    upper_count = sum(1 for char in line if char.isupper())  # 대문자 개수
    digit_count = sum(1 for char in line if char.isdigit())  # 숫자 개수
    space_count = sum(1 for char in line if char.isspace())  # 공백 개수
    
    # 결과 출력
    print(lower_count, upper_count, digit_count, space_count)