def check(x1,y1,x2,y2,x3,y3):
    X = x1 * y2 + x2 * y3 + x3 * y1
    Y = y1 * x2 + y2 * x3 + y3 * x1

    if X - Y == 0: return 0
    elif X - Y > 0: return 1
    else: return -1

# =================================

x1,y1=map(int,(input().split()))
x2,y2=map(int,(input().split()))
x3,y3=map(int,(input().split()))

print(check(x1,y1,x2,y2,x3,y3))

