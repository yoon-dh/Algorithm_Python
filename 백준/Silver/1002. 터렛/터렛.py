import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = list(map(int, input().split()))
    add = (r1 + r2) ** 2
    sub = (r1 - r2) ** 2
    distance = (x2 - x1) ** 2 + (y2 - y1) ** 2

    if (distance == 0) and (sub == 0): print(-1)
    elif (distance == add) or (distance == sub): print(1)
    elif (sub < distance) and (distance < add): print(2)
    else: print(0)