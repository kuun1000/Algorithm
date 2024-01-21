s = input()
length = len(s)

if length % 2 == 0: # 단어의 길이가 짝수인 경우
    # 앞 문자열과 뒤집은 뒷 문자열 비교
    result = (s[:length // 2] == s[length // 2: ][::-1])

else: # 단어의 길이가 홀수인 경우
    # 가운데 문자를 제외하고, 앞 문자열과 뒤집은 뒷 문자열 비교
    result = (s[:length // 2] == s[length // 2 + 1:][::-1])

print(int(result))