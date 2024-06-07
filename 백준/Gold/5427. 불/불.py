from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(arr, x, y, fire):
    user_q = deque()
    fire_q = deque()
    user_q.append((x,y))
    arr[x][y] = 0

    # 불위치 큐에 넣기
    for fx, fy in fire:
        fire_q.append((fx,fy))

    result = 0   # 출력 값
    while user_q:
        
        # 불 이동
        for _ in range(len(fire_q)):
            fx,fy = fire_q.popleft()
            for i in range(4):
                nx = fx + dx[i]
                ny = fy + dy[i]

                if arr[nx][ny] == '#':
                    continue
                elif arr[nx][ny] == '*':
                    continue
                elif arr[nx][ny] == -1:
                    continue
                else:
                    arr[nx][ny] = '*'
                    fire_q.append((nx,ny))

        # 사람 이동
        user_cnt = 0
        for _ in range(len(user_q)):
            ux, uy = user_q.popleft()        
            for i in range(4):
                nx = ux + dx[i]
                ny = uy + dy[i]
                
                if arr[nx][ny] == -1:              
                    return result+1
                
                elif str(arr[nx][ny]).isdigit():
                    continue
                elif arr[nx][ny] == '#':
                    continue
                elif arr[nx][ny] == '*':
                    continue
                else:         
                    arr[nx][ny] = 0    # 방문함(표시)
                    user_cnt = 1
                    user_q.append((nx,ny))
        result += user_cnt

        if len(user_q) == 0:
            return 'IMPOSSIBLE'           

for _ in range(int(input())):
    n,m =  map(int, input().split())
    arr = [[-1]*(n+2)]
    
    for i in range(m):
        tmp = list(input().strip())
        tmp.insert(0,-1)
        tmp.append(-1)
        arr.append(tmp)
    arr.append([-1]*(n+2))

    fire = []    # 불의 위치
    for i in range(1,m+1):
        for j in range(1,n+1):  
            if arr[i][j] == '@':
                x = i     # 출발 위치
                y = j     # 출발 위치
            elif arr[i][j] == '*':
                fire.append((i,j))
    
    result = bfs(arr, x, y, fire)
    print(result)