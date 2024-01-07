from collections import deque

dx = [-1,1,0,0]
dy = [0,0,1,-1]
dz = [-1,1]

def BFS(S,E):
    Q = deque()
    Q.append(S)
    visited = [[[0]*M for _ in range(N)] for _ in range(L)]

    while Q:
        x,y,z = Q.popleft()

        if arr[z][x][y] == 'E':
            print(f'Escaped in {visited[z][x][y]} minute(s).')
            return

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < N and 0 <= ny < M and arr[z][nx][ny] != '#' and visited[z][nx][ny] == 0:
                Q.append((nx,ny,z))
                visited[z][nx][ny] = visited[z][x][y] + 1

        for idx in range(2):
            nz = z + dz[idx]
            if 0<= nz < L and arr[nz][x][y] != '#' and visited[nz][x][y] == 0:
                Q.append((x,y,nz))
                visited[nz][x][y] = visited[z][x][y] + 1

    else:
        print('Trapped!')
        return

# ================================================

while True:
    L,N,M = map(int,input().split())
    if L == 0: break

    arr = []
    for _ in range(L):
        temp = [list(input()) for _ in range(N)]
        garbage = list(input())
        arr.append(temp)

    S = (0,0,0) # x,y,z
    E = (0,0,0)

    for l in range(L):
        for i in range(N):
            for j in range(M):
                if arr[l][i][j] == 'S': S = (i,j,l)
                elif arr[l][i][j] == 'E': E = (i,j,l)

    BFS(S,E)
