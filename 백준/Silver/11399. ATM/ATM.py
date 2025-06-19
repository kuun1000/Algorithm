import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
times.sort()

cumulated = 0
total = 0
for time in times:
    cumulated += time
    total += cumulated

print(total)