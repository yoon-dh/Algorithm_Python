from collections import deque
import sys
input = sys.stdin.readline

def T_sort():
    Q = deque()
    for i in range(1, N + 1):
        if line_count[i] == 0:
            Q.append(i)
            time_cnt[i] = time[i]

    while Q:
        now = Q.popleft()
        for i in G[now]:
            line_count[i] -= 1
            time_cnt[i] = max(time_cnt[now] + time[i], time_cnt[i])  
            if line_count[i] == 0:
                Q.append(i)
# ==========================================

T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    time = [0] + list(map(int,input().split()))
    G = [[] for _ in range(N + 1)]
    line_count = [0] * (N + 1)
    time_cnt = [0 for _ in range(N+1)]

    for _ in range(K):
        s,e = map(int,input().split())
        G[s].append(e)
        line_count[e] += 1

    target = int(input())
    T_sort()
    print(time_cnt[target])
