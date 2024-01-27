from collections import deque
import sys, heapq
input = sys.stdin.readline

def T_sort():
    Q = []
    for i in range(1,N+1):
        if line_cnt[i] == 0:
            heapq.heappush(Q,i)

    ans = []
    while Q:
        current_node = heapq.heappop(Q)
        ans.append(current_node)
        for i in G[current_node]:
            line_cnt[i] -= 1
            if line_cnt[i] == 0:
                heapq.heappush(Q,i)

    print(' '.join(map(str,ans)))

# ==========================================

N,M = map(int,input().split())
G = [[] for _ in range(N+1)]
line_cnt = [0 for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    G[A].append(B)
    line_cnt[B] += 1

T_sort()