import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[sys.maxsize] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    arr[i][i] = 0

for _ in range(m):
    x, y, distance = map(int, input().split())
    arr[x][y] = distance
    arr[y][x] = distance

result = [[j for j in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    result[i][i] = '-'

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > arr[i][k]+arr[k][j]:
                arr[i][j] = arr[i][k]+arr[k][j]
                result[i][j] = result[i][k]

for i in result[1:]:
    print(*i[1:])