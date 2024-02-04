import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(x, y):
    for a, b in G[x]:
        if V[a] == -1:
            V[a] = y + b
            dfs(a, y + b)

# ==========================================
n = int(input())
G = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    G[a].append([b, c])
    G[b].append([a, c])

V = [-1] * (n + 1)
V[1] = 0
dfs(1, 0)

S = V.index(max(V))

V = [-1] * (n + 1)
V[S] = 0
dfs(S, 0)

print(max(V))