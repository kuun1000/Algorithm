import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewels.sort(key=lambda x: x[0])
bags.sort()


total = 0
heap = []
j = 0

for bag in bags:
    while j < n and bag >= jewels[j][0]:
        heapq.heappush(heap, -jewels[j][1])
        j += 1

    if heap:
        total += (-1 * heapq.heappop(heap))

print(total)