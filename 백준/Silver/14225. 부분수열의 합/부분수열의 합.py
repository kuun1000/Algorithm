import sys
input = sys.stdin.readline


def find_num(total, start):
    possible.add(total)
    
    for i in range(start, len(s)):
        find_num(total + s[i], i + 1)



n = int(input())
s = list(map(int, input().split()))

possible = set()

find_num(0, 0)

i = 1
while i in possible:
    i += 1

print(i)