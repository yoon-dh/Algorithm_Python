from copy import deepcopy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dict = {'1': [[0], [1], [2], [3]],
        '2': [[0, 1], [2, 3]],
        '3': [[0, 3], [1, 3], [1, 2], [0, 2]],
        '4': [[0, 1, 2], [0, 2, 3], [1, 2, 3], [0, 1, 3]],
        '5': [[0, 1, 2, 3]]}


def check(dir, cur_r, cur_c, arr_copy):
    cnt, nr, nc = 0, cur_r, cur_c
    while True:
        nr += dr[dir]
        nc += dc[dir]
        if 0 <= nr < N and 0 <= nc < M and arr_copy[nr][nc] != '6':
            if arr_copy[nr][nc] == '0':
                arr_copy[nr][nc] = '#'
        else:
            return arr_copy


def search_dfs(n, cctv_dir):
    global ans, arr, dict

    if n == len(cctv_pos):
        arr_copy = deepcopy(arr)

        for idx, dirs in enumerate(cctv_dir):
            cur_r, cur_c = cctv_pos[idx][0], cctv_pos[idx][1]
            for d in dirs:
                arr_copy = check(d, cur_r, cur_c, arr_copy)

        result = 0
        for c in range(N):
            result += arr_copy[c].count('0')
        if ans > result:
            ans = result
        return

    r, c = cctv_pos[n][0], cctv_pos[n][1]
    for idx, dir in enumerate(dict[arr[r][c]]):
        cctv_dir.append(dir)
        search_dfs(n + 1, cctv_dir)
        cctv_dir.pop()


N, M = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]
cctv_pos = []
ans = 0xffffff
for i in range(N):
    for j in range(M):
        if arr[i][j] != '#' and 0 < int(arr[i][j]) < 6:
            cctv_pos.append([i, j])

search_dfs(0, [])
print(ans)



