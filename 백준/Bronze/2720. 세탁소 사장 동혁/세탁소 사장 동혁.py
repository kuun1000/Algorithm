import sys

# 변수 입력 및 선언
t = int(sys.stdin.readline())
changes = [25, 10, 5, 1] # 쿼터, 다임, 니켈, 페니

for _ in range(t):
    c = int(sys.stdin.readline())

    # 각 동전 별로
    for change in changes:
        print(c // change, end=" ") # 동전의 개수 = 거스름돈 // 동전 금액
        c %= change # 남은 금액 = 거스름돈 % 동전 금액
    print()