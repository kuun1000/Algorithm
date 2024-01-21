n = int(input())

for i in range(n-1, -1, -1):
    print(" " * i, end="") 
    print("*" * (2 * (n - i) - 1))

for j in range(1, n):
    print(" " * j, end="")
    print("*" * (2 * (n - j) - 1))