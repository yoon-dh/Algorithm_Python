N = int(input())

dp = [[] for _ in range(N+1)]
dp[1] += [1]

for i in range(2,N+1):
    dp[i] = dp[i-1] + [i]
    if not i % 3:
        if len(dp[i//3]) + 1 < len(dp[i]):
            dp[i] = dp[i//3] + [i]
    if not i % 2:
        if len(dp[i//2]) + 1 < len(dp[i]):
            dp[i] = dp[i//2] + [i]

print(len(dp[N]) - 1)
print(*dp[N][::-1])