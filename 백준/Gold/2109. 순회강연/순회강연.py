import heapq
import sys
input = sys.stdin.readline

n = int(input())
fees = [list(map(int, input().split())) for _ in range(n)]

fees.sort(key=lambda x: x[1])

heap = []

for p, d in fees:
    heapq.heappush(heap, p)

    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))