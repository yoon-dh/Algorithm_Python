from collections import deque
import sys
input = sys.stdin.readline


def T_sort():
    Q = deque()
    dp = [0] * (N+1)
    for i in range(1, N + 1):
        if line_cnt[i] == 0:
            Q.append(i)
            dp[i] = time_lst[i]
    while Q:
        current_node = Q.popleft()
        for i in G[current_node]:
            line_cnt[i] -= 1
            dp[i] = max(dp[i],dp[current_node] + time_lst[i])
            if line_cnt[i] == 0:
                Q.append(i)

    return max(dp)

# ======================================================

N = int(input())
G = [[] for _ in range(N+1)]
line_cnt = [0] * (N+1)
time_lst = [0]

for i in range(1, N+1):
    input_list = list(map(int, input().split()))
    time_lst.append(input_list[0])
    if input_list[1] != 0:
        for j in range(2, len(input_list)):
            G[input_list[j]].append(i)
            line_cnt[i] += 1

print(T_sort())