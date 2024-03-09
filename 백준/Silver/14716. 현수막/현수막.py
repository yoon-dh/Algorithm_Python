from collections import deque

def BFS(arr):
    Q = deque()

    dr = [1,-1,0,0,1,1,-1,-1]
    dc = [0,0,1,-1,1,-1,1,-1]

    cnt = 0
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 1:
                Q.append((x,y))
                arr[x][y] = '.'
                cnt += 1
                while Q:
                    r,c = Q.popleft()
                    for idx in range(8):
                        nr = r + dr[idx]
                        nc = c + dc[idx]
                        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                            Q.append((nr,nc))
                            arr[nr][nc] = '.'

    return cnt


N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

print(BFS(arr))