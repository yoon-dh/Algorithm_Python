import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

ans = 0xffffff

for i in range(3):
    dp = [[1001] * 3 for _ in range(n)]
    dp[0][i] = lst[0][i]
    for j in range(1,n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + lst[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + lst[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + lst[j][2]
    dp[-1][i] = 0xffffff
    ans = min(ans,min(dp[-1]))

print(ans)
