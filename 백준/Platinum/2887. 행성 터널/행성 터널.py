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
    elif a > b:parent[a] = b

def kruskal(edge_lst):
    global ans
    for i in range(len(edge_lst)):
        if find(parent,edge_lst[i][1]) != find(parent,edge_lst[i][2]):
            union(parent,edge_lst[i][1],edge_lst[i][2])
            ans += edge_lst[i][0]

    return print(ans)

# ============================================================

n = int(input())
parent = [i for i in range(n)]
lst = []

for i in range(n):
    x,y,z = map(int,input().split())
    lst.append((x,y,z,i))

edge_lst = []
for i in range(3):
    lst.sort(key=lambda x:x[i])
    for k in range(1,n):
        edge_lst.append((abs(lst[k - 1][i] - lst[k][i]), lst[k - 1][3], lst[k][3]))

ans = 0
edge_lst.sort()
kruskal(edge_lst)