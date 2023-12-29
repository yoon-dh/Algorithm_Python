N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0][0],dp[0][1],dp[0][2] = arr[0][0],arr[0][1],arr[0][2]

for i in range(1,N):
    for j in range(3):
        if j == 0: dp[i][j] = min(dp[i-1][1],dp[i-1][2]) + arr[i][j]
        elif j == 1: dp[i][j] = min(dp[i-1][0],dp[i-1][2]) + arr[i][j]
        else: dp[i][j] = min(dp[i-1][0],dp[i-1][1]) + arr[i][j]
print(min(dp[N-1]))