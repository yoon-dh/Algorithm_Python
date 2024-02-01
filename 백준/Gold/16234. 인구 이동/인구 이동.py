from collections import deque
from copy import deepcopy

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def move_cycle():

    divide_array = []
    divide_sum = []

    visited = [[0] * N for _ in range(N)]
    is_change = True

    for i in range(len(arr)):
        for j in range(len(arr)):
            if visited[i][j] == 0:
                Q = deque()
                Q.append((i,j))
                union_lst = []
                union_sum = 0
                while Q:
                    r,c = Q.popleft()
                    visited[r][c] = "X"
                    if (r,c) not in union_lst:
                        union_lst.append((r,c))
                        union_sum += arr[r][c]
                    for idx in range(4):
                        nr, nc = r + dr[idx] , c + dc[idx]
                        if 0 <= nr < N and 0 <= nc < N and (L <= abs(arr[r][c] - arr[nr][nc]) <= R):
                            if visited[nr][nc] != "X":
                                Q.append((nr,nc))
                                union_lst.append((nr,nc))
                                union_sum += arr[nr][nc]
                                visited[nr][nc] = "X"

                divide_array.append(union_lst)
                divide_sum.append(union_sum)

    for i in range(len(divide_array)):
        move_result = divide_sum[i] // len(divide_array[i])
        for j in range(len(divide_array[i])):
            x,y = divide_array[i][j]
            arr[x][y] = move_result

    if len(divide_array) == N ** 2:
        is_change = False

    return is_change


# =========================================

N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

cnt = 0
while True:
    ans = move_cycle()
    if not ans:
        print(cnt)
        break
    cnt += 1
