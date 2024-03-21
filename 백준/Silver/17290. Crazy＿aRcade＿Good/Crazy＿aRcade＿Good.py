import sys
input = sys.stdin.readline

def append_pos(char):
    lst = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == char:
                lst.append((i, j))
    return lst

# ====================================================

x1,y1 = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(10)]
n = 10

bomb_pos = append_pos('o')

dr = [-1,1,0,0]
dc = [0,0,1,-1]

for r,c in bomb_pos:
    for idx in range(4):
        for k in range(10):
            nr = r + dr[idx] * k
            nc = c + dc[idx] * k
            if 0 <= nr < n and 0 <= nc < n:
                arr[nr][nc] = 'o'

safe_pos = append_pos('x')

Min = 0xffffff
for x,y in safe_pos:
    Min = min(Min,abs(x1-1-x) + abs(y1-1-y))

print(Min)

