from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    visited = [[0] * m for _ in range(n)]
    Q = deque()
    Q.append((0, 0))
    visited[0][0] = 1

    while Q:
        r, c = Q.popleft()
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if arr[nr][nc] >= 1: arr[nr][nc] += 1
                else:
                    Q.append((nr, nc))
                    visited[nr][nc] = 1

def melt():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0
                cnt += 1
            elif arr[i][j] >= 2:
                arr[i][j] = 1
    return cnt

# ============================================================

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

hour = 0
while True:
    bfs()
    if melt():hour += 1
    else:
        print(hour)
        break