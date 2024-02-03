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
    line_cnt = 0
    for cost,a,b in edge_list:
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
            ans += cost
            line_cnt += 1

    return ans,line_cnt

# =================================

N,M = map(int,input().split())
M_or_W = [0] + list(input().split())
parent = [i for i in range(N+1)]
edge_lst = []

for _ in range(M):
    a,b,cost = map(int,input().split())
    if M_or_W[a] == M_or_W[b]: continue
    edge_lst.append((cost,a,b))

edge_lst.sort()
ans,line_cnt = kruskal(edge_lst)
if line_cnt == N - 1: print(ans)
else: print(-1)