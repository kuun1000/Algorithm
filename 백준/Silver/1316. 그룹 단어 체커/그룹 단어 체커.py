n = int(input())
cnt = n
for word in [input() for _ in range(n)]:
    if any(word[i] != word[i+1] and word[i] in word[i+1:] for i in range(len(word) - 1)):
        cnt -= 1
print(cnt)