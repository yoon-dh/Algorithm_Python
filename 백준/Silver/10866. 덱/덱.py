import sys
from collections import deque

deque_list = deque()

n = int(input())

for _ in range(n):
    a = sys.stdin.readline().split()

    if a[0] == 'push_back': deque_list.append(a[1])
    if a[0] == 'push_front': deque_list.appendleft(a[1])

    if a[0] == 'pop_front':
        if len(deque_list) != 0: print(deque_list.popleft())
        else: print(-1)

    if a[0] == 'pop_back':
        if len(deque_list) != 0: print(deque_list.pop())
        else: print(-1)

    if a[0] == 'size': print(len(deque_list))

    if a[0] == 'empty':
        if len(deque_list) != 0: print(0)
        else: print(1)

    if a[0] == 'front':
        if len(deque_list) != 0: print(deque_list[0])
        else: print(-1)

    if a[0] == 'back':
        if len(deque_list) != 0: print(deque_list[-1])
        else: print(-1)
