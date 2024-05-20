import sys
input = sys.stdin.readline

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def backtracking(r, c, visited, total):
    global ans
    if len(visited) == N + 1:
        ans += total
        return

    for idx in range(4):
        nr = r + dr[idx]
        nc = c + dc[idx]
        if (nr, nc) not in visited:
            visited.append((nr, nc))
            backtracking(nr, nc, visited, total * percent[idx])
            visited.pop()

# ===============================================================

N, ep, wp, sp, np = map(int, input().split())
percent = [ep, wp, sp, np]
ans = 0

backtracking(0, 0, [(0, 0)], 1)
print(ans * (0.01 ** N))
