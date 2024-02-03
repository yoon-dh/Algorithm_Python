import sys, heapq
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

def dijkstra(node_list,start_node):
    distance = [0xfffffff for _ in range(N)]
    distance[start_node] = 0
    hq = []
    heapq.heappush(hq,[0,start_node])

    while hq:
        current_dist,current_node = heapq.heappop(hq)
        if distance[current_node] < current_dist: continue
        for next_node, next_dist in node_list[current_node]:
            if distance[next_node] > current_dist + next_dist:
                distance[next_node] = current_dist + next_dist
                heapq.heappush(hq,[current_dist + next_dist, next_node])
    return distance

def kruskal(edge_list):
    ans = 0
    node_list = [[] for _ in range(N)]
    for cost,a,b in edge_list:
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
            ans += cost
            node_list[a].append([b,cost])
            node_list[b].append([a,cost])
    print(ans)

    Max = 0
    for i in range(N):
        distance = dijkstra(node_list,i)
        Max = max(Max,sorted(distance)[-1])
    print(Max)

# ====================================================

N,M = map(int,input().split())
parent = [i for i in range(N)]
edge_lst = []
for _ in range(M):
    a,b,cost = map(int,input().split())
    edge_lst.append((cost,a,b))

edge_lst.sort()
kruskal(edge_lst)
