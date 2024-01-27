from collections import deque
import sys
input = sys.stdin.readline

def T_sort():
    Q = deque()
    for i in range(1,N+1):
        if line_cnt[i] == 0:
            Q.append(i)

    result = []
    while Q:
        current_node = Q.popleft()
        result.append(current_node)
        for i in G[current_node]:
            line_cnt[i] -= 1
            if line_cnt[i] == 0:
                Q.append(i)

    return result

# ====================================

N,M = map(int,input().split())
G = [[] for _ in range(N+1)]
line_cnt = [0 for _ in range(N+1)]

for _ in range(M):
    temp = list(map(int,input().split()))
    for i in range(1,len(temp)-1):
        G[temp[i]].append(temp[i+1])
        line_cnt[temp[i+1]] += 1

ans = T_sort()
if len(ans) != len(line_cnt) - 1: print(0)
else:
    for i in ans:
        print(i)