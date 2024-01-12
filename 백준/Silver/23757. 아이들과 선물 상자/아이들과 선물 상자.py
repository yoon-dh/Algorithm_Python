from collections import deque
import sys,heapq
input = sys.stdin.readline

N,M = map(int,input().split())
gift = list(map(int,input().split()))
kids = deque(list(map(int,input().split())))

gift_heap = []

for i in range(len(gift)):
    heapq.heappush(gift_heap,(-gift[i],gift[i]))


for i in range(len(kids)):
    max_gift = heapq.heappop(gift_heap)[1]
    cur_kids = kids.popleft()
    if max_gift > cur_kids:
        heapq.heappush(gift_heap,(-(max_gift - cur_kids),max_gift - cur_kids))
    elif max_gift == cur_kids:
        continue
    else:
        print(0)
        break
else:
    print(1)
