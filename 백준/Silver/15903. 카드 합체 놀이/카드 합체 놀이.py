import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())

hq = []
lst = [int(i) for i in input().split()]

for i in lst:
    heapq.heappush(hq, i)

for _ in range(m):
    c1 = heapq.heappop(hq)
    c2 = heapq.heappop(hq)
    heapq.heappush(hq, c1 + c2)
    heapq.heappush(hq, c1 + c2)

print(sum(hq))