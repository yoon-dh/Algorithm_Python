import heapq
import sys

input = sys.stdin.readline

n = int(input())

min_heap = []

for _ in range(n):
    item = int(input())
    if item != 0: heapq.heappush(min_heap, item)
    else:
        if len(min_heap) == 0:
            print(0)
            continue
        else:
            Min = heapq.heappop(min_heap)
            print(Min)

