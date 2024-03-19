from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

dr = [-1,1,0,0]
dc = [0,0,1,-1]

def BFS(lst):
    Q = deque()
    visited = [[-1] * n for i in range(n)]
    virus_cnt = 0

    for r,c in lst:
        Q.append((r,c))
        visited[r][c] = 0
        virus_cnt += 1

    for r,c in wall:
        visited[r][c] = '.'

    ans = 0
    while Q:
        r,c = Q.popleft()
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                if visited[nr][nc] > Min: break
                Q.append((nr,nc))
                virus_cnt += 1
                ans = max(ans,visited[nr][nc])

    return ans, virus_cnt

# ================================================

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

can_put_virus = []
wall = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: wall.append((i,j))
        elif arr[i][j] == 2: can_put_virus.append((i,j))


answer_virus = n * n - len(wall)
Min = 0xffffff

for i in combinations(can_put_virus,m):
    result, virus_cnt = BFS(list(i))
    if virus_cnt == answer_virus: Min = min(Min,result)

if Min == 0xffffff: print(-1)
else: print(Min)