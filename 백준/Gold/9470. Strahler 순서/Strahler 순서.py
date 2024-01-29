from collections import deque
import sys
input = sys.stdin.readline

def T_sort():
    Q = deque()
    stahler_lst = [[0, 0] for _ in range(M + 1)]
    for i in range(1,M+1):
        if line_cnt[i] == 0:
            Q.append(i)
            stahler_lst[i] = [1,1]

    while Q:
        current_node = Q.popleft()
        Max, cnt = stahler_lst[current_node]
        if cnt >= 2: node_stahler = Max + 1
        else: node_stahler = Max

        for k in G[current_node]:
            line_cnt[k] -= 1
            if stahler_lst[k][0] < node_stahler:
                stahler_lst[k][0] = node_stahler
                stahler_lst[k][1] = 1
            elif stahler_lst[k][0] == node_stahler:
                stahler_lst[k][1] += 1
            else:
                pass

            if line_cnt[k] == 0: Q.append(k)

    return stahler_lst[-1]

# ========================================================

T = int(input())
for _ in range(T):
    K,M,P = map(int,input().split())
    G = [[] for _ in range(M+1)]
    line_cnt = [0] * (M+1)
    for _ in range(P):
        s,e = map(int,input().split())
        G[s].append(e)
        line_cnt[e] += 1

    ans = T_sort()
    if ans[1] >= 2: print(f'{K} {ans[0]+1}')
    else: print(f'{K} {ans[0]}')