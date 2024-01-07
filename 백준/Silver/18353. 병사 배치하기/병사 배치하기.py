n = int(input())
lst = [0] + list(map(int,input().split()))[::-1]

dp = [0] * (n+1)

for i in range(1,n+1):
    Max = 0
    for j in range(0,i):
        if lst[i] > lst[j]:
            Max = max(Max,dp[j])
    dp[i] = Max + 1

print(len(lst) - max(dp) - 1)