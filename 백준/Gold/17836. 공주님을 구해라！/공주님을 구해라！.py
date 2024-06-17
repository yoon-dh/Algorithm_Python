from collections import deque
import sys
input = sys.stdin.readline

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def bfs():
    global ans
    Q = deque([[0,0]])

    while Q:
        r,c = Q.popleft()

        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != 1 and visited[nr][nc] == 0:
                if arr[nr][nc] == 0:
                    Q.append([nr,nc])
                    visited[nr][nc] = visited[r][c] + 1
                    if nr == n - 1  and nc == m - 1:
                        ans = min(ans,visited[nr][nc])
                        return
                else:
                    visited[nr][nc] = visited[r][c] + 1
                    ans = min(ans, visited[nr][nc] + get_sword)


# ======================================================

n,m,time = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

get_sword = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            get_sword = (n - i - 1) + (m - j - 1)

ans = 0xffffff

bfs()

if ans > time : print("Fail")
else: print(ans)