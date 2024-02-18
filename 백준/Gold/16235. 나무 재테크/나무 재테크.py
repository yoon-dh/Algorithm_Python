import sys
input = sys.stdin.readline
from collections import deque


def spring_summer():
    for i in range(n):
        for j in range(n):
            for k in range(len(tree_Q[i][j])):
                if land[i][j] < tree_Q[i][j][k]:
                    for _ in range(k, len(tree_Q[i][j])):
                        dead_lst[i][j].append(tree_Q[i][j].pop())
                    break
                else:
                    land[i][j] -= tree_Q[i][j][k]
                    tree_Q[i][j][k] += 1

    for i in range(n):
        for j in range(n):
            while dead_lst[i][j]:
                land[i][j] += dead_lst[i][j].pop() // 2

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def autumn_winter():
    for i in range(n):
        for j in range(n):
            for k in range(len(tree_Q[i][j])):
                if tree_Q[i][j][k] % 5 == 0:
                    for t in range(8):
                        nr = i + dr[t]
                        nc = j + dc[t]
                        if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
                        tree_Q[nr][nc].appendleft(1)

            land[i][j] += a[i][j]

# ======================================================================

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
land = [[5] * n for _ in range(n)]
tree_Q = [[deque() for _ in range(n)] for _ in range(n)]
dead_lst = [[list() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree_Q[x - 1][y - 1].append(z)

while True:
    if k == 0:
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += len(tree_Q[i][j])
        print(ans)
        break

    spring_summer()
    autumn_winter()

    k -= 1
