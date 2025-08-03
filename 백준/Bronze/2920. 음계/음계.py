import sys
input = sys.stdin.readline

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

arr = list(map(int, input().split()))
n = len(arr)

if arr == ascending:
    print("ascending")
elif arr == descending:
    print("descending")
else:
    print("mixed")