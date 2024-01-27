import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x > y: parent[x] = y
    else : parent[y] = x

N, M = map(int, input().split())
parent = [i for i in range(N)]

for i in range(M):
    s,e = map(int,input().split())
    if find(s) == find(e):
        print(i + 1)
        break
    union(s,e)
else: print(0)