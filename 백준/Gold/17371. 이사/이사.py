import sys
input = sys.stdin.readline

def calc(i,j):
    return (point[i][0]-point[j][0])**2+(point[i][1]-point[j][1])**2

# ================================================

n=int(input())
point = [tuple(map(int,input().split())) for _ in range(n)]

Max=int(1e9)

for i in range(n):
    temp=0

    for j in range(n):
        temp = max(temp,calc(i,j))

    if Max > temp:
        Max = temp
        ans = i

print(*point[ans])