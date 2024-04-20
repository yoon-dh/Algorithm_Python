import sys
input = sys.stdin.readline
from math import sqrt

x, y, d, t = map(int, input().split())
distance = sqrt(x ** 2 + y ** 2)

if d <= distance: answer = min(t * (distance // d) + distance % d, t * (distance // d + 1),distance)
else: answer = min(t + (d - distance), 2 * t, distance)
print(answer)