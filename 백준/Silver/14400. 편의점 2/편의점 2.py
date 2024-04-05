import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: x[0])
x = arr[N // 2][0]

arr.sort(key=lambda x: x[1])
y = arr[N // 2][1]

ans = 0
for i in range(N):
    ans += (abs(arr[i][0] - x) + abs(arr[i][1] - y))

print(ans)