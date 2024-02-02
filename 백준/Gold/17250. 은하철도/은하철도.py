import sys
input = sys.stdin.readline

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b: parent[b] = a; dp[a] += dp[b]
    elif a > b:parent[a] = b; dp[b] += dp[a]

N,M = map(int,input().split())

parent = [i for i in range(N+1)]
dp = [0] * (N+1)

for i in range(N):
    dp[i+1] = int(input())

for i in range(M):
    a,b = map(int,input().split())
    union(parent,a,b)
    a_parent = find(parent,a)
    b_parent = find(parent,b)
    print(dp[min(a_parent,b_parent)])
