from collections import deque
import sys
input = sys.stdin.readline

def T_sort():
    Q = deque()
    for i in range(1,N+1):
        if line_cnt[i] == 0:
            Q.append((i,1))

    depth = 1
    result = [0 for _ in range(N+1)]

    while Q:
        current_node, current_depth = Q.popleft()
        if current_depth != depth:
            depth += 1

        result[current_node] = current_depth
        for i in G[current_node]:
            line_cnt[i] -= 1
            if line_cnt[i] == 0:
                Q.append((i,depth + 1))

    return result[1:]

# =========================================

N,M = map(int,input().split())
G = [[] for _ in range(N+1)]
line_cnt = [0 for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,input().split())
    G[s].append(e)
    line_cnt[e] += 1

print(*T_sort())