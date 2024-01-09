def DFS(n,sm):
    global Max
    if n == 11:
        Max = max(Max,sm)
        return

    for i in range(11):
        if arr[n][i] == 0: continue
        if used[i]: continue

        used[i] = 1
        DFS(n+1, sm+arr[n][i])
        used[i] = 0


T = int(input())
for _ in range(T):
    arr = [list(map(int,input().split())) for _ in range(11)]
    used = [0] * 11
    Max = 0
    DFS(0,0)

    print(Max)