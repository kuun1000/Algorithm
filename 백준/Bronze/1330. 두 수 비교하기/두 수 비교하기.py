A, B = tuple(map(int, input().split()))

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")