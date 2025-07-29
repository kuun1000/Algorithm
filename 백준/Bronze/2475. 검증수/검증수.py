numbers = list(map(int, input().split()))
squared = [num ** 2 for num in numbers]

print(sum(squared) % 10)