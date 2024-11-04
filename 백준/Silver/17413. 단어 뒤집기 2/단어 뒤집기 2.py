s = list(input())

in_tag = False
word = []
result = []
for character in s:
    if character == "<":
        if word:
                result.extend(word[::-1])
                word = []
        in_tag = True
        result.append(character)
    elif character == ">":
        in_tag = False
        result.append(character)
    elif in_tag:
        result.append(character)
    elif not in_tag:
        if character == " ":
            result.extend(word[::-1])
            result.append(character)
            word = []
        else:
            word.append(character)
if word:
     result.extend(word[::-1])

print("".join(result))