import sys 
input = sys.stdin.readline

n = int(input())
expression = input().strip()
values = [int(input().strip()) for _ in range(n)]


operand_values = {chr(65 + i): values[i] for i in range(n)}

stack = []

for char in expression:
    if char.isalpha(): 
        stack.append(operand_values[char])  
    else: 
        b = stack.pop()
        a = stack.pop()
        if char == "+":
            stack.append(a + b)
        elif char == "-":
            stack.append(a - b)
        elif char == "*":
            stack.append(a * b)
        elif char == "/":
            stack.append(a / b)

result = stack.pop()
print(f"{result:.2f}")