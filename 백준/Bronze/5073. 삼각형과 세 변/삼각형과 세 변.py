while True:
    lengths = list(map(int, input().split()))
    if 0 in lengths:
        break
    if sum(lengths) - max(lengths) <= max(lengths):
        print("Invalid")
    elif len(set(lengths)) == 1:
        print("Equilateral")
    elif len(set(lengths)) == 2:
        print("Isosceles")
    else:
        print("Scalene")