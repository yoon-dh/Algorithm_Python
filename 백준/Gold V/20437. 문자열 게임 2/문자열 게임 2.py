import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
for _ in range(T):
    W = input().rstrip()
    K = int(input())
    len_str = len(W)

    alpha = defaultdict(list)

    for i in range(len_str):
        if W.count(W[i]) >= K:
            alpha[W[i]].append(i)

    if not alpha:
        print(-1)
        continue

    Min = 0xffffff
    Max = 0

    for lst in alpha.values():
        for j in range(len(lst) - K + 1):
            tmp = lst[j + K - 1] - lst[j] + 1
            if tmp < Min: Min = tmp
            if tmp > Max: Max = tmp

    print(f'{Min} {Max}')
