n = int(input())
m = int(input())

if m != 0:  
    broken = list(map(int, input().split()))
else:
    broken = []

# 1. +, - 버튼만 이용
min_press = abs(n - 100)

# 2. 숫자 버튼 이용
for num in range(1000000):
    str_num = str(num)
    for digit in str_num:
        if int(digit) in broken:
            break
    else:
        presses = len(str_num) + abs(n - num)
        min_press = min(min_press, presses)
print(min_press)