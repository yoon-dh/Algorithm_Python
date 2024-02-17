
import heapq

n = int(input())

hq = []
for i in range(n):
    a = int(input())
    if i == 0:
        vote = a
        continue

    heapq.heappush(hq, -a)

ans = 0
while hq:
    a = -heapq.heappop(hq)
    if a < vote:
        break

    vote += 1
    ans += 1
    heapq.heappush(hq, -(a - 1))

print(ans)