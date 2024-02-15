import sys
input = sys.stdin.readline

INF = float('inf')
n = int(input())
m = int(input())
lst = [[INF] * (n + 1) for _ in range(n + 1)]
prev = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if lst[a][b] > c:
        lst[a][b] = c
        prev[a][b] = a

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and lst[i][j] > lst[i][k] + lst[k][j]:
                lst[i][j] = lst[i][k] + lst[k][j]
                prev[i][j] = prev[k][j]

for i in lst[1:]:
    tmp = []
    for j in i[1:]:
        if j == INF: tmp.append(0)
        else: tmp.append(j)
    print(*tmp)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if lst[i][j] == INF: print(0)
        else:
            route = [j]
            tmp = j
            while tmp != i:
                route.append(prev[i][tmp])
                tmp = prev[i][tmp]

            print(len(route), end=' ')
            print(*route[::-1])
