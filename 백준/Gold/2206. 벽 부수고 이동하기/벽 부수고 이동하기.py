from collections import deque

dr = [-1,1,0,0]
dc = [0,0,1,-1]

def BFS(x,y,z):
    Q = deque()
    Q.append((x,y,z))
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[x][y][z] = 1

    while Q:
        a,b,c = Q.popleft()
        if a == N - 1 and b == M - 1:
            return visited[a][b][c]

        for idx in range(4):
            nr = a + dr[idx]
            nc = b + dc[idx]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if arr[nr][nc] == 1 and c == 0:
                visited[nr][nc][1] = visited[a][b][0] + 1
                Q.append((nr,nc,1))
            elif arr[nr][nc] == 0 and visited[nr][nc][c] == 0:
                visited[nr][nc][c] = visited[a][b][c] + 1
                Q.append((nr,nc,c))

    return -1

# ====================================================

N,M = map(int, input().split())
arr = [list(map(int,input())) for _ in range(N)]

print(BFS(0,0,0))