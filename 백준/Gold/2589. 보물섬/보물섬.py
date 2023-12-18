import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n) :
    one = input()
    one = list(one)
    board.append(one)

dx = [1,0,-1,0]
dy = [0,-1,0,1]


def lroad(y,x) :
    que = deque()
    visited = [[0] * m for _ in range(n)]

    que.append([y,x,0])
    visited[y][x] = 1

    answer = 0

    while que :
        y,x,count = que.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m :
                if visited[ny][nx] == 0 and board[ny][nx] == "L":
                    visited[ny][nx] = 1
                    newcount = count + 1
                    que.append([ny,nx,newcount])

                    answer = max(answer, newcount)

    return answer

answer = 0

for i in range(n) :
    for j in range(m) :
        if board[i][j] == "L" :
            hubo = lroad(i,j)
            answer = max(answer, hubo)

print(answer)