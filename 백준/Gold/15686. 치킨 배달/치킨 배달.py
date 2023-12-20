from collections import deque
from itertools import combinations

def chicken(arr):
    c_lst = []
    h_lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                c_lst.append((i,j))
            if arr[i][j] == 1:
                h_lst.append((i,j))

    return list(combinations(c_lst,M)), h_lst


def BFS():
    c_pos,h_pos = chicken(arr)

    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    cnt = 9999999
    for i in c_pos:
        Q = deque()
        visited = [[-1]*N for _ in range(N)]
        for k in i:
            Q.append(k)
            visited[k[0]][k[1]] = 0
        while Q:
            r,c = Q.popleft()
            for idx in range(4):
                nr = r + dr[idx]
                nc = c + dc[idx]
                if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc] != -1 or visited[nr][nc] == 0:
                    continue
                Q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1

        total = 0
        for x,y in h_pos:
            total += visited[x][y]
        cnt = min(cnt,total)

    return cnt

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

print(BFS())