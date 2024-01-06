
import sys
from collections import deque

def bfs():

    queue = deque()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1:
                    queue.append((i, j, k, 0))


    dh = [1, -1, 0, 0, 0, 0]
    dn = [0, 0, 1, -1, 0, 0]
    dm = [0, 0, 0, 0, 1, -1]
    d = 0
    while queue:
        z, x, y, d = queue.popleft()
        for i in range(6):
            th = z + dh[i]
            tn = x + dn[i]
            tm = y + dm[i]
            if 0 <= th < h and 0 <= tn < n and 0 <= tm < m and arr[th][tn][tm] == 0:
                arr[th][tn][tm] = 1
                queue.append((th, tn, tm, d + 1))

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 0:
                    return -1
    return d


m, n, h = map(int, sys.stdin.readline().split())
arr = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
print(bfs())
