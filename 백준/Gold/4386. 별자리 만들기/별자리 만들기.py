import sys
input = sys.stdin.readline

def distance(x1,y1,x2,y2):
    return ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5

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
    result = 0
    for edge in edges:
        cost,node1,node2 = edge
        if find(parent,node1) != find(parent,node2):
            union(parent,node1,node2)
            result += cost

    return result
# ===========================================

n = int(input())
parent = [i for i in range(n+1)]
star_lst = []
edge_lst = []

for _ in range(n):
    x,y = map(float,input().split())
    star_lst.append((x,y))

for i in range(n - 1):
    for j in range(i + 1,n):
        edge_lst.append((distance(star_lst[i][0],star_lst[i][1], star_lst[j][0],star_lst[j][1]),i,j))

edge_lst.sort()
ans = kruskal(edge_lst)
print(round(ans,2))