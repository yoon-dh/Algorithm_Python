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
    cnt = 0
    ans = 0
    for cost,a,b  in edge_list:
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
            ans += cost + (t * cnt)
            cnt += 1

    return ans

# =================================================

N,M,t = map(int,input().split())
parent = [i for i in range(N+1)]
edge_lst = []
for _ in range(M):
    a,b,cost = map(int,input().split())
    edge_lst.append((cost,a,b))

edge_lst.sort()
print(kruskal(edge_lst))