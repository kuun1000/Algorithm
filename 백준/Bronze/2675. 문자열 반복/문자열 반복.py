for _ in range(int(input())):
    r, s = input().split()
    r = int(r)

    p = [x * r for x in s]
    print("".join(p))
