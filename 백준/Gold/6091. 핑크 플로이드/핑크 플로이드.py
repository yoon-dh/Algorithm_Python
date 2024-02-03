import sys,heapq
input = sys.stdin.readline

def find(parent,x):
  if parent[x] != x:
    parent[x] = find(parent,parent[x])
  return parent[x]

# ===================================

N = int(input())
parent = [i for i in range(N+1)]
tree = [[] for i in range(N+1)]

lst = []
for i in range(1,N):
  temp = [*map(int,input().split())]
  for j in range(i+1,N+1):
    heapq.heappush(lst,(temp[j-1-i],i,j))

for i in range(N-1):
  while True:
    w,a,b = heapq.heappop(lst)
    if find(parent,a) == find(parent,b): continue
    parent[parent[a]] = parent[b]
    tree[a].append(b)
    tree[b].append(a)
    break

for i in range(1,N+1):
  print(len(tree[i]),*sorted(tree[i]))