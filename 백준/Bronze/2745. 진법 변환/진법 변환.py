n, b = input().split()
b = int(b)

num = 0
for idx, digit in enumerate(n):
    if digit.isalpha():
        num += (ord(digit) - 55) * (b**(len(n) - idx - 1))
    else:
        num += int(digit) * (b**(len(n) - idx - 1))
print(num)