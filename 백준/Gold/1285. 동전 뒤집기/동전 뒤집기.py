import sys
input = sys.stdin.readline

def check(n):
    for i in range(N):
        arr[i][n] = abs(arr[i][n] - 1)

# =======================================

N = int(input())

arr = []
for i in range(N):
    arr.append([*map(lambda x: 1 if x == "T" else 0, input().rstrip())])

ans = N ** 2
L = 0
for i in range(1 << N):
    for n in range(N):
        if (i ^ L) & (1 << n): check(n)
    ans = min(ans, sum(map(lambda x: min(sum(x), N - sum(x)), arr)))
    L = i

print(ans)