import sys
input = sys.stdin.readline

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a in know and b in know: return
    if a in know: parent[b] = a
    elif b in know: parent[a] = b
    else:
        if a < b: parent[b] = a
        else: parent[a] = b

N,M = map(int,input().split())
know = set(list(map(int,input().split()))[1:])
parent = [i for i in range(N+1)]
party_lst = []

for _ in range(M):
    party = list(map(int,input().split()))[1:]
    for i in range(len(party)-1):
        union(parent,party[i],party[i+1])
    party_lst.append(party)

ans = 0
for i in party_lst:
    for j in range(len(i)):
        if find(parent,i[j]) in know:
            break
    else: ans += 1

print(ans)
