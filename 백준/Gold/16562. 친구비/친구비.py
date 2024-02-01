import sys
input = sys.stdin.readline

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if lst[a] < lst[b]: parent[b] = a
    else: parent[a] = b

# =================

N,M,K = map(int,input().split())
lst = [0] + list(map(int,input().split()))
parent = [i for i in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    union(parent,a,b)

set_parent = list(set(parent))

friends = set()
ans = 0

for i in range(1, N + 1):
    if find(parent,i) not in friends:
        ans += lst[parent[i]]
        friends.add(parent[i])

if ans > K:print("Oh no")
else: print(ans)