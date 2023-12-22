from collections import deque

def BFS(arr):
    Q = deque()

    dr = [-1,1,0,0,1,1,-1,-1]
    dc = [0,0,1,-1,1,-1,-1,1]

    cnt = 0
    for x in range(h):
        for y in range(w):
            if arr[x][y] == 1:
                Q.append((x,y))
                arr[x][y] = 0
                cnt += 1
                while Q:
                    r,c = Q.popleft()
                    for idx in range(8):
                        nr = r + dr[idx]
                        nc = c + dc[idx]
                        if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1:
                            Q.append((nr,nc))
                            arr[nr][nc] = 0
    return cnt

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0: break

    arr = []
    for _ in range(h):
        arr.append(list(map(int,input().split())))

    print(BFS(arr))
