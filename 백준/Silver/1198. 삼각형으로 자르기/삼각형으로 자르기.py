from itertools import combinations
import sys
input = sys.stdin.readline


def triangle(x, y, z):
    return abs((x[0]*y[1]+y[0]*z[1]+z[0]*x[1]-x[1]*y[0]-y[1]*z[0]-z[1]*x[0]))/2

# ==========================================

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

ans = []
for i,j,k in combinations(arr, 3):
    ans.append(triangle(i, j, k))

print(max(ans))