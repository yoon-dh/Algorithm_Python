import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x:x[1]) 

min_heap = []
cnt = 0

for i in arr:
    while min_heap and min_heap[0]<=i[1]: 
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, i[2])
    cnt = max(cnt, len(min_heap))

print(cnt)
