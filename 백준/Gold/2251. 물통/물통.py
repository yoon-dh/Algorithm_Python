from collections import deque

def pour(x,y):
    if not visit[x][y]:
        visit[x][y]=True
        Q.append((x,y))

def bfs():
    Q.append((0,0)) 
    visit[0][0]=True
    while Q:
        x,y=Q.popleft()
        z=c-x-y
        if x==0:
            ans.append(z)
        
        water=min(x,b-y)
        pour(x-water,y+water)
        water=min(x,c-z)
        pour(x-water,y)
        water=min(y,a-x)
        pour(x+water,y-water)
        water=min(y,c-z)
        pour(x,y-water)
        water=min(z,a-x)
        pour(x+water,y)
        water=min(z,b-y)
        pour(x,y+water)

a, b, c = map(int, input().split())
Q = deque()
ans = []
visit = [[False]*(b+1) for _ in range(a+1)]
bfs()
ans.sort()
print(' '.join(map(str, ans)))