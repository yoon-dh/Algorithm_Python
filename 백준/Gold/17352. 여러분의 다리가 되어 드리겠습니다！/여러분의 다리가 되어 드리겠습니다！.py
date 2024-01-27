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


N = int(input())
parent = [i for i in range(N+1)]

for _ in range(N-2):
    s,e = map(int,input().split())
    union(s,e)

for i in range(2,N+1):
    if find(1) != find(i):
        print(1,i)
        break