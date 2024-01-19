# 입력을 42로 나눴을 때의 나머지 
remainders = [int(input()) % 42 for _ in range(10)]

# set 자료형으로 변환 -> 중복 제거
remainders = set(remainders)

print(len(remainders))