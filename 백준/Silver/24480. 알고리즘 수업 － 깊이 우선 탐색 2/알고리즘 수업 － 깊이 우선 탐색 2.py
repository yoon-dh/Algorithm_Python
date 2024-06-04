import sys
sys.setrecursionlimit(100000)

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0

def dfs(v):
    global cnt
    cnt += 1
    visited[v] = cnt
    for nv in sorted(graph[v], reverse=True):
        if not visited[nv]:
            dfs(nv)


dfs(R)
print('\n'.join(map(str, visited[1:])))