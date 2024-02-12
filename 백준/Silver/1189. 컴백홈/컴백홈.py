def DFS(n,pos,visited):
    global ans
    if n == K-1:
        if pos == [0,C-1]:
            ans += 1
            return
        else: return

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    r,c = pos[0],pos[1]

    for idx in range(4):
        nr,nc = r + dr[idx], c + dc[idx]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != 'T' and visited[nr][nc] == 0:
            visited[nr][nc] = visited[r][c] + 1
            DFS(n+1,[nr,nc],visited)
            visited[nr][nc] = 0
            nr = r
            nc = c



R,C,K = map(int,input().split())
arr = [list(input()) for _ in range(R)]

V = [[0]*C for _ in range(R)]
V[R-1][0] = 1

ans = 0
DFS(0,[R-1,0],V)
print(ans)