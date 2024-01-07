T = int(input())
dp = [0,1,1,1,2,2,3,4,5,7,9]
for _ in range(T):
    n = int(input())
    if n < len(dp):
        print(dp[n])
    else:
        for i in range(len(dp), n+1):
            dp.append(dp[i-1] + dp[i-5])
        print(dp[n])