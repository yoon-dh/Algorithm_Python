import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    V,E = map(int,input().split())
    x = 2 - V + E
    print(x)
    