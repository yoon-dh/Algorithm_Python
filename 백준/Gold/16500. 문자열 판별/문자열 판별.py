import sys
input = sys.stdin.readline

def check(x):
    global ans
    if x == len(S):
        ans = 1
        return
    if dp[x]: return
    dp[x] = 1
    for i in range(len(lst)):
        if len(S[x:]) >= len(lst[i]):
            for j in range(len(lst[i])):
                if lst[i][j] != S[x+j]: break
            else: check(x+len(lst[i]))
    return

S = input().rstrip()
N = int(input())
lst = [input().rstrip() for _ in range(N)]
dp = [0] * 101

ans = 0
check(0)
print(ans)
