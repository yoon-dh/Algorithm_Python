import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int,input().split()))

    ans = 0
    Max = stock[-1]

    for i in range(N-2,-1,-1):
        if stock[i] > Max: Max = stock[i]
        else: ans += (Max - stock[i])

    print(ans)