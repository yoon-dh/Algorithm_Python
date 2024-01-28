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

def kruskal(edges):
    ans = 0
    for edge in edges:
        cost,node1,node2 = edge
        if find(parent,node1) != find(parent,node2):
            union(parent,node1,node2)
            ans += cost
    return ans

# =============================================

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
parent = [i for i in range(N)]
edge_lst = []

for i in range(N):
    for j in range(i+1,N):
        edge_lst.append((arr[i][j],i,j))

edge_lst.sort()
print(kruskal(edge_lst))