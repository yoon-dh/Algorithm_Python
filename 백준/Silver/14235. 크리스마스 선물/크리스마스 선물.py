import sys,heapq
input = sys.stdin.readline

n = int(input())
gift = []
for _ in range(n):
    a = list(map(int,input().split()))
    if a[0] == 0:
        if len(gift) == 0: print(-1)
        else: print(heapq.heappop(gift)[1])
    else:
        for i in range(1,len(a)):
            heapq.heappush(gift,(-a[i],a[i]))


