ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

if ax1 > bx1:
    ax1, bx1 = bx1, ax1
    ay1, by1 = by1, ay1
    ax2, bx2 = bx2, ax2
    ay2, by2 = by2, ay2

if ax2 == bx1:
    if ay2 == by1 or ay1 == by2: print("POINT");
    elif ay1 <= by1 <= ay2 or ay1 <= by2 <= ay2 or by1 <= ay1 <= by2: print("LINE")
    exit();
elif ax2 > bx1:
    if by2 < ay1 or ay2 < by1: print("NULL")
    elif by2 == ay1 or ay2 == by1: print( "LINE")
    else: print("FACE")
    exit();

print("NULL")