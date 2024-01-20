s = input()

# 알파벳별 처음 등장 위치에 대한 배열
pos = [-1] * 26
for elem in s:
    pos[ord(elem) - ord('a')] = s.index(elem)

print(*pos)