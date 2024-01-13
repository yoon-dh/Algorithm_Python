import sys
input = sys.stdin.readline

n,k = map(int,input().split())

lst = []
for _ in range(n): lst.append(int(input()))


coin = sorted(set(lst))
dp = [0xffffff] * (k+1)
dp[0] = 0

for i in coin:
    for j in range(1,k+1):
        if j-i >= 0:
            dp[j] = min(dp[j],dp[j-i]+1)

if dp[k] == 0xffffff: print(-1)
else: print(dp[k])
