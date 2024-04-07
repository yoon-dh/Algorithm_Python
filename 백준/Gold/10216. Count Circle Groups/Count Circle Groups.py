import sys
from math import sqrt


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    parent = [i for i in range(n)]

    for i in range(n - 1):
        for j in range(i, n):
            x1, y1, r1 = arr[i]
            x2, y2, r2 = arr[j]
            if sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= r1 + r2:
                union(parent, i, j)

    SET = set()
    for i in range(n):
        x = find(parent, i)
        if x not in SET: SET.add(x)

    print(len(SET))