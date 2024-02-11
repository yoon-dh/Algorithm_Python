import sys
input = sys.stdin.readline

def check_min(start_team,link_team):
    start = link = 0
    for i in range(M):
        for j in range(M):
            start += arr[start_team[i]][start_team[j]]
            link += arr[link_team[i]][link_team[j]]
    return abs(start-link)

def dfs(n,start_team,link_team):
    global ans
    if n == N:
        if len(start_team) == len(link_team):
            ans = min(ans,check_min(start_team,link_team))
        return

    dfs(n+1,start_team + [n], link_team)
    dfs(n+1,start_team, link_team + [n])

# ===================================================

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
M = N//2

ans = 0xffffff
dfs(0,[],[])
print(ans)