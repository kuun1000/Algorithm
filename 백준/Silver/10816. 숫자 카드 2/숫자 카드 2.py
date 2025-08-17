import sys
input = sys.stdin.readline

n = int(input())
arr_n = list(map(int, input().split()))

m =  int(input())
arr_m = list(map(int, input().split()))

arr_n.sort()
numbers = {}
for elem in arr_n:
    if elem not in numbers:
        numbers[elem] = 1
    else:
        numbers[elem] += 1

for elem in arr_m:
    if elem in numbers:
        print(numbers[elem], end=" ")
    else:
        print(0, end=" ")