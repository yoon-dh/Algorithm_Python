from collections import deque

dr = [-1,1,0,0]
dc = [0,0,1,-1]

def BFS():
    global visited,arr
    Q = deque()
    start = None
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                Q.append((i,j))
                start = (i,j)
                visited[i][j] = 'S'
                break

    while Q:
        r,c = Q.popleft()

        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0 and visited[nr][nc] == -1:
                Q.append((nr,nc))
                if visited[r][c] == "S": visited[nr][nc] = 1
                else: visited[nr][nc] = visited[r][c] + 1

    visited[start[0]][start[1]] = 0

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            visited[i][j] = -1

BFS()

for i in visited:
    print(*i)


