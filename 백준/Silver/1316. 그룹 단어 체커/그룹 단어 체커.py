n = int(input())
cnt = n

for _ in range(n):
    word = input()
    # 각 단어에 대해
    for i in range(len(word) - 1):
        # 다음 문자와 같은 경우 -> 그 다음 문자로 넘어감
        if word[i] == word[i+1]:
            continue
        # 다음 문자와 다르고, 이후에 등장하는 경우 -> 그룹 단어 X
        elif word[i] in word[i+1:]:
            cnt -= 1    # 전체 단어 개수에서 1 감소시킴
            break
print(cnt)