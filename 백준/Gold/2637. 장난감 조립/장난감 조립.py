from collections import deque
import sys
input = sys.stdin.readline

def T_sort():
    Q = deque()
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        if line_cnt[i] == 0:
            Q.append(i)
            dp[i][i] = 1

    while Q:
        current_node = Q.popleft()
        for next_node,cnt in G[current_node]:
            for k in range(1,N+1):
                dp[next_node][k] += dp[current_node][k] * cnt
            line_cnt[next_node] -= 1
            if line_cnt[next_node] == 0:
                Q.append(next_node)

    return dp[-1]

# =================================================

N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]
line_cnt = [0] * (N+1)


for _ in range(M):
    e,s,cnt = map(int,input().split())
    G[s].append((e,cnt))
    line_cnt[e] += 1

ans = T_sort()

for i in range(1,len(ans)):
    if ans[i] != 0:
        print(f'{i} {ans[i]}')