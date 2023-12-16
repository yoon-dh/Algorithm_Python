import sys

import heapq
import copy
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())
arr = [[0] * c for _ in range(r)]
V = [[0] * c for _ in range(r)]
water_q = deque()
q = deque()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
swan_list = []

for i in range(r):
    k = input()
    for j in range(c):
        arr[i][j] = k[j]
        if arr[i][j] == "." or arr[i][j] == "L":
            water_q.append((i, j))
        if arr[i][j] == "L":
            swan_list.append((i, j))

q.append(swan_list[0])
V[swan_list[0][0]][swan_list[0][1]] = 1
day = 0


def bfs():
    global day
    global q
    global water_q
    while True:
        next_q = deque()
        ending = False

        while (q):
            x, y = q.popleft()
            if x == swan_list[1][0] and y == swan_list[1][1]:
                ending = True

            for i in range(4):
                n_x = x + dx[i]
                n_y = y + dy[i]
                if 0 <= n_x < r and 0 <= n_y < c and V[n_x][n_y] == 0:
                    V[n_x][n_y] = 1
                    if arr[n_x][n_y] == "X":
                        next_q.append((n_x, n_y))
                    else:
                        q.append((n_x, n_y))

        if ending:
            break

        q = copy.deepcopy(next_q)

        cnt = len(water_q)

        while (cnt != 0):
            cnt -= 1
            x, y = water_q.popleft()
            for i in range(4):
                n_x = x + dx[i]
                n_y = y + dy[i]
                if 0 <= n_x < r and 0 <= n_y < c and V[n_x][n_y] == 0:
                    if arr[n_x][n_y] == "X":
                        arr[n_x][n_y] = "."
                        water_q.append((n_x, n_y))
        day += 1


bfs()
print(day)

