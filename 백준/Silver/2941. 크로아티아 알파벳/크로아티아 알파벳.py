# 크로아티아 알파벳
croatians = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
for croatian in croatians:
    # 2 ~ 3개로 이루어진 경우, 하나의 문자로 변경 
    s = s.replace(croatian, '*')

print(len(s))