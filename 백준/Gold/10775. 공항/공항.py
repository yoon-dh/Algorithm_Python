# 탑승구 1 ~ G번
# P개의 비행기가 차례대로 도착할 예정
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

# =======================================

G = int(input())
P = int(input())

parent = [i for i in range(0,G+1)]

cnt = 0

for _ in range(P):
    check = find(parent,int(input()))
    if check == 0: break
    union(parent,check,check - 1)
    cnt += 1

print(cnt)


