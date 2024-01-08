import heapq
import sys

input = sys.stdin.readline

n = int(input())

max_heap = []
for _ in range(n):
    item = int(input())
    if item != 0: heapq.heappush(max_heap, (-item, item))
    else:
        heapq.heappush(max_heap, (-item, item))
        Max = heapq.heappop(max_heap)
        print(Max[1])