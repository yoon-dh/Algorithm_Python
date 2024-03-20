from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(p):
    visited = [[[0] * 64 for _ in range(M)] for _ in range(N)]
    Q = deque()
    total_cnt = -1
    x, y = p
    Q.append((x, y, 0))
    visited[x][y][0] = 1

    while Q:
        r, c, tz = Q.popleft()
        if arr[r][c] == '1':
            total_cnt = visited[r][c][tz] - 1
            break
        for idx in range(4):
            x = r + dr[idx]
            y = c + dc[idx]

            if not (0 <= x < N and 0 <= y < M and visited[x][y][tz] == 0 and arr[x][y] != '#'):
                continue

            if arr[x][y] in ['a', 'b', 'c', 'd', 'e', 'f']:
                z = tz | (1 << (ord(arr[x][y]) - ord('a')))
                if visited[x][y][z] == 0:
                    visited[x][y][z] = visited[r][c][tz] + 1
                    Q.append((x, y, z))

            elif arr[x][y] in ['A', 'B', 'C', 'D', 'E', 'F']:
                if tz & (1 << (ord(arr[x][y]) - ord('A'))):
                    visited[x][y][tz] = visited[r][c][tz] + 1
                    Q.append((x, y, tz))

            else:
                visited[x][y][tz] = visited[r][c][tz] + 1
                Q.append((x, y, tz))
    return total_cnt

# ==================================================

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            print(bfs((i,j)))

