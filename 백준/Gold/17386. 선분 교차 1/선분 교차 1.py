import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    v1 = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
    v2 = p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0]
    result = v1 - v2
    if result > 0: return 1
    elif result < 0: return -1
    return 0

# ==================================================

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
p1, p2, p3, p4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]
A = ccw(p1, p2, p3) * ccw(p1, p2, p4)
B = ccw(p3, p4, p1) * ccw(p3, p4, p2)

if A == -1 and B == -1: print(1)
else: print(0)