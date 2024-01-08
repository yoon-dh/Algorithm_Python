from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

enter_Q = deque()
out_Q = deque()

for i in range(n*2):
    if i < n: enter_Q.append(input())
    else: out_Q.append(input())


out_car = set()
cnt = 0
while out_Q:
    if enter_Q[0] in out_car:
        enter_Q.popleft()
        continue
    out = out_Q.popleft()
    if enter_Q[0] != out:
        out_car.add(out)
        cnt += 1
    else:
        enter_Q.popleft()

print(cnt)