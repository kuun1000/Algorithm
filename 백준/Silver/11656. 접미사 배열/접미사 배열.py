s = list(input())

prefix = []
for i in range(len(s)):
    prefix.append(''.join(s[i:]))

prefix.sort()

for elem in prefix:
    print(elem)