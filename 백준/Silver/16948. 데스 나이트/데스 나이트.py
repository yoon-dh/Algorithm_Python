from collections import deque

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def BFS(start):
    Q = deque()
    Q.append(start)
    arr[start[0]][start[1]] = 0

    while Q:
        x,y = Q.popleft()
        if arr[x][y] == 'E':
            return arr[x][y]
        for idx in range(6):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < n and (arr[nx][ny] == 0 or arr[nx][ny] =='E'):
                if arr[nx][ny] == 'E':
                    return arr[x][y] + 1
                else:
                    Q.append((nx,ny))
                    arr[nx][ny] = arr[x][y] + 1
    return -1

n = int(input())
r1,c1,r2,c2 = map(int,input().split())

arr = [[0] * n for _ in range(n)]
arr[r1][c1] = 'S'
arr[r2][c2] = 'E'
start = (r1,c1)

print(BFS(start))