import sys,math
input = sys.stdin.readline

def square(x1,y1):
    x_min, x_max = x, x + w
    y_min, y_max = y, y + h
    return x_min <= x1 <= x_max and y_min <= y1 <= y_max

def left_half_circle(x1,y1):
    return math.sqrt((x - x1) ** 2 + ((y + r) - y1) ** 2) <= r

def right_half_circle(x1,y1):
    return math.sqrt(((x + w) - x1) ** 2 + ((y + r) - y1) ** 2) <= r

def check(x1,y1):
    if square(x1,y1): return 1
    if left_half_circle(x1,y1): return 1
    if right_half_circle(x1,y1): return 1
    return 0

# =================================

w,h,x,y,p = map(int,input().split())
r = h/2

cnt = 0
for _ in range(p):
    x1,y1 = map(int,input().split())
    cnt += check(x1,y1)

print(cnt)