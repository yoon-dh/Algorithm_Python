import sys
input = sys.stdin.readline


h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]

dot = line = 0

for i in range(h):
    cnt = 0
    for j in range(w):
        if arr[i][j] == "/" or arr[i][j] == "\\":
            line += 1
            cnt += 1
        else:
            if cnt % 2 == 1:
                dot += 1

print(dot + (line // 2))