# 입력 받은 단어를 대문자로 변경
s = input().upper()

d = {}  # 알파벳별 등장 횟수
for elem in s:
    if elem in d:    # 딕셔너리에 존재하는 경우    
        d[elem] += 1    # 등장 횟수 1 더함
    else:            # 딕셔너리에 존재하지 않는 경우
        d[elem] = 1     # 딕셔너리에 추가 

# 등장 횟수가 최댓값인 알파벳 
max_keys = [k for k,v in d.items() if max(d.values()) == v]

if len(max_keys) == 1: 
    print(max_keys[0])
else:
    print("?")