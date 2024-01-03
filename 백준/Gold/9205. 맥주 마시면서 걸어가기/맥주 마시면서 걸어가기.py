from collections import deque

def BFS():
    Q = deque()
    Q.append((home_X,home_Y))

    while Q:
        x,y = Q.popleft()
        if abs(x-end_X) + abs(y-end_Y) <= 1000:
            print('happy')
            return
        for i in range(N):
            if not visited[i]:
                nx,ny = store_list[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    Q.append((nx,ny))
                    visited[i] = 1
    else:
        print('sad')
        return

# ====================================================

T = int(input())

for _ in range(T):
    N = int(input())
    home_X,home_Y = map(int,input().split())
    store_list = []
    for _ in range(N):
        store_X, store_Y = map(int,input().split())
        store_list.append((store_X,store_Y))

    end_X,end_Y = map(int,input().split())
    visited = [0] * (N+1)
    BFS()

