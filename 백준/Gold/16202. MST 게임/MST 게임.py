from collections import deque
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
    parent = [i for i in range(N+1)]
    MST_cost = 0
    mst_edge = []
    line_cnt = 0
    for cost,a,b in edge_list:
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
            MST_cost += cost
            line_cnt += 1
            mst_edge.append((cost,a,b))

    return MST_cost,mst_edge,line_cnt

# ======================================================================

N,M,K = map(int,input().split())
edge_lst = []
for i in range(1,M+1):
    a,b = map(int,input().split())
    edge_lst.append((i,a,b))

edge_lst.sort()
MST_cost, mst_edge, line_cnt = kruskal(edge_lst)

edge_lst_set = set(list(edge_lst))
mst_Q = deque(sorted(mst_edge))
if line_cnt == N-1: result = [MST_cost]
else: result = [0]

for _ in range(K-1):
    Min_cost_edge = mst_Q.popleft()
    edge_lst_set.discard(Min_cost_edge)
    turn_MST_cost,turn_mst_edge,turn_line_cnt = kruskal(sorted(edge_lst_set))
    mst_Q = deque(turn_mst_edge)
    if turn_line_cnt == N-1: result.append(turn_MST_cost)
    else: result.append(0)

print(*result)
