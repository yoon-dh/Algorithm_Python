'''
1. FD x : 거북이를 x 만큼 앞으로 전진
2. LT a : 거북이를 반시계 방향으로 a도 만큼 회전
3. RT a : 거북이를 시계 방향으로 a도 만큼 회전
4. PU : 연필을 올린다
5. PD : 연필을 내린다
'''

import sys
input = sys.stdin.readline
from collections import deque

dr = [0,1,0,-1]
dc = [-1,0,1,0]

def remove(x,y):
    Q = deque()
    Q.append([x,y])
    arr[x][y] = 0
    while Q:
        r, c = Q.popleft()
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if 0<=nr<2001 and 0<=nc<2001 and arr[nr][nc]:
                Q.append([nr,nc])
                arr[nr][nc] = 0


def draw(s_x,s_y,t_x,t_y):
    for y in range(s_y,t_y+1):
        arr[t_x][y] = 1
        arr[s_x][y] = 1
    for x in range(s_x,t_x+1):
        arr[x][s_y] = 1
        arr[x][t_y] = 1

# =======================================================

N = int(input())
arr = [[0]*2001 for _ in range(2001)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    draw(2*(x1+500),2*(y1+500),2*(x2+500),2*(y2+500))

ans = -1 if arr[1000][1000] else 0
for i in range(2001):
    for j in range(2001):
        if arr[i][j]==1:
            remove(i,j)
            ans += 1
print(ans)