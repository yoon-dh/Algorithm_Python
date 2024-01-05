import sys
input = sys.stdin.readline
for i in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    if x3 > x2 or x4 < x1 or y3 > y2 or y4 < y1:
        print('d')
        continue

    if [x1, y1] == [x4, y4] or [x2, y1]==[x3, y4] or [x1, y2] == [x4, y3] or [x2, y2] == [x3, y3]:
        print('c')
        continue

    if x4 == x1 and y4 > y1 and y2 > y3:
        print('b')
        continue
    if y4 == y1 and x2 > x3 and x4 > x1:
        print('b')
        continue
    if x3 == x2 and y4 > y1 and y2 > y3:
        print('b')
        continue
    if y3 == y2 and x2 > x3 and x4 > x1:
        print('b')
        continue

    print('a')