import sys
input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    arr.append([int(i) for i in input().split()])

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1

for row in arr:
    print(' '.join(map(str,row)))