from collections import deque

dir_dict = {"U": [0,1],"D": [0,-1],"L": [-1,0],"R": [1,0]}

def solution(dirs):
    dirs = deque(list(dirs))
    Q = deque()
    Q.append((0,0))

    cnt = 0
    visited = []
    
    while dirs:
        x,y = Q.popleft()
        dx,dy = dir_dict[dirs.popleft()]
        nx = x + dx
        ny = y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if [(x,y),(nx,ny)] not in visited and [(nx,ny),(x,y)] not in visited:
                visited.append([(x,y),(nx,ny)])
                x,y = nx,ny
                Q.append((x,y))
                cnt += 1
            else:
                Q.append((nx,ny))
        else:
            Q.append((x,y))
    
    return cnt
        
        
        
    
    