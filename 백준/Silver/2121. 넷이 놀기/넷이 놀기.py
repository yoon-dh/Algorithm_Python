import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
xy = set(tuple(map(int, input().split())) for _ in range(N))

ans = 0
for x,y in xy:
    if ((x+A,y) in xy) and ((x,y+B) in xy) and ((x+A,y+B) in xy):
        ans += 1

print(ans)
