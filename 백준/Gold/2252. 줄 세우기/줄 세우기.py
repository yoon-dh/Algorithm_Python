from collections import deque
import sys
input = sys.stdin.readline

def T_sort():
    Q = deque()
    for i in range(1,N+1):
        if line_count[i] == 0:
            Q.append(i)
    result = []
    while Q:
        now = Q.popleft()
        result.append(now)
        for i in G[now]:
            line_count[i] -= 1
            if line_count[i] == 0:
                Q.append(i)

    return result
# ===============================

N,M = map(int,input().split())
G = [[] for _ in range(N+1)]
line_count = [0 for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,input().split())
    G[s].append(e)
    line_count[e] += 1

ans = T_sort()
print(*ans)