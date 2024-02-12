def dfs(current,cnt):
    global ans
    if current == N:
        ans = max(ans, cnt)
        return

    if egg_list[current][0] <= 0: dfs(current+1,cnt)
    else:
        flag = False
        for i in range(N):
            if i == current or egg_list[i][0] <= 0: continue
            flag = True
            egg_list[current][0] -= egg_list[i][1]
            egg_list[i][0] -= egg_list[current][1]
            dfs(current + 1, cnt + int(egg_list[current][0] <= 0) + int(egg_list[i][0] <= 0))
            egg_list[current][0] += egg_list[i][1]
            egg_list[i][0] += egg_list[current][1]

        if flag == False: dfs(current + 1,cnt)

# =================================================

N = int(input())
egg_list = [list(map(int,input().split())) for _ in range(N)]

# 내구도,무게
ans = 0
dfs(0,0)
print(ans)