import sys
input = sys.stdin.readline


expression = list(input().rstrip().split('-'))

result = 0
for i in range(len(expression)):
    numbers = list(map(int, expression[i].split('+')))
    
    if i == 0:
        result += sum(numbers)
    else:
        result -= sum(numbers)

print(result)