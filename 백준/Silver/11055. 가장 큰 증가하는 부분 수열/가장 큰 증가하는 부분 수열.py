n = int(input())
lst = list(map(int,input().split()))

dp = list(lst)


for i in range(1,n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + lst[i])

print(sorted(dp)[-1])

    