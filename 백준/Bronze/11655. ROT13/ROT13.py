s = list(input())

for elem in s:
    if elem.isupper():
            print(chr((ord(elem) - ord('A') + 13) % 26 + ord('A')), end="")
    elif elem.islower():
         print(chr((ord(elem) - ord('a') + 13) % 26 + ord('a')), end="")
    else:
        print(elem, end="")