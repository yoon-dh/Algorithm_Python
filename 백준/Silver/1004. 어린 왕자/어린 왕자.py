import sys
from math import dist

input = sys.stdin.readline

for i in range(int(input())):
    x, y, a, b = map(int, input().split())

    A, B = (x, y),(a, b)

    cnt = 0

    for l in range(int(input())):
        x1, y1, C = map(int, input().split())
        center = (x1, y1)
        if dist(A, center) <= C and dist(B, center) > C: cnt += 1
        elif dist(A, center) > C and dist(B, center) <= C: cnt += 1

    print(cnt)