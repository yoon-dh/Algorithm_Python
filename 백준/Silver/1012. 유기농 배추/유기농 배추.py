from collections import deque

def BFS(arr):
    Q = deque()

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    cnt = 0
    for x in range(M):
        for y in range(N):
            if arr[x][y] == 1:
                Q.append((x,y))
                arr[x][y] = 0
                cnt += 1
                while Q:
                    r,c = Q.popleft()
                    for idx in range(4):
                        nr = r + dr[idx]
                        nc = c + dc[idx]
                        if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 1:
                            Q.append((nr,nc))
                            arr[nr][nc] = 0

    return cnt

for tc in range(int(input())):
    N,M,K = map(int,input().split())
    arr = [[0]*N for _ in range(M)]

    for _ in range(K):
        x,y = map(int,input().split())
        arr[y][x] = 1

    print(BFS(arr))
