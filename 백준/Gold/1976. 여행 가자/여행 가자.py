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

# =================

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

arr = [list(map(int,input().split())) for _ in range(N)]
travel_lst = list(map(int,input().split()))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            union(parent,i+1,j+1)

parent_num = parent[travel_lst[0]]
cnt = 0
for i in travel_lst:
    cnt += parent[i]

if cnt / len(travel_lst) == parent_num: print('YES')
else: print('NO')
