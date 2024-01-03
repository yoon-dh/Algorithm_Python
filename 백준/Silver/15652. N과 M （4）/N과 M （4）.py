def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(start, N + 1):
        s.append(i)
        dfs(i)
        s.pop()

s = []
N, M = map(int, input().split())

dfs(1)