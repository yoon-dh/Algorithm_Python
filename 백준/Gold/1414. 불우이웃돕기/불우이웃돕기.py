import string
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

# =============================================

alpha_list = list(string.ascii_letters)
alpha_dict = dict()
for i in range(len(alpha_list)):
    alpha_dict[alpha_list[i]] = i + 1

N = int(input())
parent = [i for i in range(N+1)]
arr = [list(input()) for _ in range(N)]
edge_list = []

total = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == '0': continue
        else:
            edge_list.append((alpha_dict[arr[i][j]],i+1,j+1))
            total += alpha_dict[arr[i][j]]

edge_list.sort()
ans,line_cnt = kruskal(edge_list)

if line_cnt == N-1: print(total - ans)
else: print(-1)
