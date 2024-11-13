import sys 
input = sys.stdin.readline

expression = list(input().strip())

op = []
for char in expression:
    if char.isalpha():
        print(char, end="")
    else:
        if char == "(":
            op.append(char)
        elif char == ")":
            while op and op[-1] != "(":
                print(op.pop(), end="")
            op.pop()
        elif char in "*/":
            while op and op[-1] in "*/":
                print(op.pop(), end="")
            op.append(char)
        elif char in "+-":
            while op and op[-1] != "(":
                print(op.pop(), end="")
            op.append(char)
while op:
    print(op.pop(), end="")