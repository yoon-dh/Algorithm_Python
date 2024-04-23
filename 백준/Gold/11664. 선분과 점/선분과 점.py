import sys
input = sys.stdin.readline

def calc(x1, y1, z1, x2, y2, z2):
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) ** (1/2)

# ========================================================

ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())

Min = 0xffffffff
SC = calc(ax, ay, az, cx, cy, cz)
EC = calc(bx, by, bz, cx, cy, cz)

while True:
    mx = (ax + bx) / 2
    my = (ay + by) / 2
    mz = (az + bz) / 2
    KC = calc(mx, my, mz, cx, cy, cz)
    if abs(Min - KC) <= 1e-6:
        print('{:.10f}'.format(KC))
        break
    Min = min(KC, Min)
    if SC < EC:
        bx, by, bz = mx, my, mz
        EC = KC
    else:
        ax, ay, az = mx, my, mz
        SC = KC