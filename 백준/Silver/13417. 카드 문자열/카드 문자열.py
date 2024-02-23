import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    Q = deque(list(input().split()))
    ans_Q = deque(Q.popleft())

    while Q:
        current = Q.popleft()
        if ord(current) <= ord(ans_Q[0]): ans_Q.appendleft(current)
        else: ans_Q.append(current)

    print(''.join(list(ans_Q)))
