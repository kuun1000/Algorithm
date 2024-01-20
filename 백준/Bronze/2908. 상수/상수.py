a, b = input().split()

# 숫자 뒤집기
a_rev, b_rev = a[::-1], b[::-1]

if a_rev > b_rev:
    print(a_rev)
else:
    print(b_rev)