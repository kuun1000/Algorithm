import sys
input = sys.stdin.readline

k = int(input())
numbers = [int(input()) for _ in range(k)]

correct = []
for num in numbers:
    if num == 0:
        correct.pop()
    else:
        correct.append(num)

print(sum(correct))