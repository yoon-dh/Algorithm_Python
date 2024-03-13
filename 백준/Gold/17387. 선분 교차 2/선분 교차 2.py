import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    v1 = [p2[0] - p1[0], p2[1] - p1[1]]
    v2 = [p3[0] - p2[0], p3[1] - p2[1]]
    return v1[0] * v2[1] - v1[1] * v2[0]


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
p1, p2, p3, p4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

if min(x1, x2) > max(x3, x4) or min(x3, x4) > max(x1, x2) or min(y1, y2) > max(y3, y4) or min(y3, y4) > max(y1, y2):
    print(0)
    exit()

A = ccw(p1, p2, p3) * ccw(p1, p2, p4)
B = ccw(p3, p4, p1) * ccw(p3, p4, p2)

if A <= 0 and B <= 0: print(1)
else: print(0)