# 인덱스: 다이얼 별 걸리는 시간 / 원소: 다이얼에 해당하는 알파벳 
dials = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

s = input()

# 입력의 각 알파벳에 대해
for alpha in s:
    # 다이얼의 모든 원소에 대해 
    for idx, dial in enumerate(dials):
        # 알파벳이 해당 원소에 포함된 경우
        if alpha in dial:
            # 인덱스를 시간에 더함
            time += idx

print(time)