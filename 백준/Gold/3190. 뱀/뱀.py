from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n = int(input())
apple_cnt = int(input())
arr = [['.'] * n for _ in range(n)]

for i in range(apple_cnt):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 'A'

l = int(input())
dir_dict = dict()
Q = deque()
Q.append((0, 0))

for i in range(l):
    x, y = input().split()
    dir_dict[int(x)] = y

r, c  = 0, 0
arr[r][c] = 'S'
time = 0
dir = 0

def change_dir(a):
    global dir
    if a == 'L': dir = (dir - 1) % 4
    else: dir = (dir + 1) % 4


while True:
    time += 1
    r += dr[dir]
    c += dc[dir]

    if r < 0 or r >= n or c < 0 or c >= n:
        break

    if arr[r][c] == 'A':
        arr[r][c] = 'S'
        Q.append((r, c))
        if time in dir_dict:
            change_dir(dir_dict[time])

    elif arr[r][c] == '.':
        arr[r][c] = 'S'
        Q.append((r, c))
        nr, nc = Q.popleft()
        arr[nr][nc] = '.'
        if time in dir_dict:
            change_dir(dir_dict[time])
    else:
        break

print(time)