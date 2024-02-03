import sys
input = sys.stdin.readline

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b: parent[b] = a
    else: parent[a] = b

def kruskal(edge_list):
    ans = 0
    for cost,a,b in edge_list:
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
            ans += cost

    return ans

# ================================

while True:
    N,M = map(int,input().split())
    if N == 0 and M == 0: break
    parent = [i for i in range(N)]
    edge_lst = []
    total = 0
    for _ in range(M):
        a,b,cost = map(int,input().split())
        edge_lst.append((cost,a,b))
        total += cost
    edge_lst.sort()
    print(total - kruskal(edge_lst))
