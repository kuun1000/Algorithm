try:
    while True:
        s = list(input())
        result = [0] * 4
        for elem in s:
            if ord("A") <= ord(elem) <= ord("Z"):
                result[1] += 1
            elif ord("a") <= ord(elem) <= ord("z"):
                result[0] += 1
            elif elem.isdigit():
                result[2] += 1
            elif elem == " ":
                result[3] += 1
        print(*result)
except EOFError:
    pass