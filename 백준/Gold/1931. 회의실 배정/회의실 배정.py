import sys
input = sys.stdin.readline

n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))

count, end = 0, 0
for meeting in meetings:
    if meeting[0] >= end:
        count += 1
        end = meeting[1]

print(count)