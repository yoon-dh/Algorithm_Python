import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

# ====================================

n, m, k = map(int, input().split())
power = list(map(int, input().split()))

parent = [0] * (n + 1)
edge_lst = []

for i in range(1, n + 1):
    if i in power: continue
    parent[i] = i

for i in range(m):
    s, e, cost = map(int, input().split())
    edge_lst.append((cost, s, e))

ans = 0
edge_lst.sort()

for edge in edge_lst:
    cost, s, e = edge
    if find(parent, s) != find(parent, e):
        union(parent, s, e)
        ans += cost

print(ans)