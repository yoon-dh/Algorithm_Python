import sys
from math import pi, atan2,sqrt

x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())

dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
if dist >= r1 + r2: ans = 0

if dist <= abs(r1 - r2): ans = pi * (min(r1, r2) ** 2)

if dist < r1 + r2 and max(r1, r2) - min(r1, r2) < dist:
    x = (r1 ** 2 - r2 ** 2 + dist ** 2) / (2 * dist)
    y = sqrt(r1 ** 2 - x ** 2)
    a1 = atan2(y, x) / pi * 180
    a2 = atan2(y, dist - x) / pi * 180
    ans = pi * (r1 ** 2) * a1 / 180 + pi * (r2 ** 2) * a2 / 180 - dist * y

print('%.3f' % ans)