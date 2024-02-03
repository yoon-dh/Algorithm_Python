import sys,heapq
input = sys.stdin.readline

N = int(input())
hq_max, hq_min = [], []

for i in range(N):
    input_num = int(input())
    if len(hq_max) == len(hq_min): heapq.heappush(hq_max, -input_num)
    else: heapq.heappush(hq_min, input_num)

    if len(hq_max) >= 1 and len(hq_min) >= 1 and -hq_max[0] > hq_min[0]:
        heapq.heappush(hq_max, heapq.heappop(hq_min) * -1)
        heapq.heappush(hq_min, heapq.heappop(hq_max) * -1)

    print(-hq_max[0])