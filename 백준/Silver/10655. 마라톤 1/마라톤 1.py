import sys
input = sys.stdin.readline


n = int(input())
distance = [0] * n
for i in range(n):
    distance[i] = list(map(int, input().split()))

Max = 0
for i in range(1, n - 1):
    temp = (abs(distance[i + 1][0] - distance[i][0]) + abs(distance[i + 1][1] - distance[i][1]) + abs(distance[i][0] - distance[i - 1][0]) + abs(distance[i][1] - distance[i - 1][1])) - (abs(distance[i + 1][0] - distance[i - 1][0]) + abs(distance[i + 1][1] - distance[i - 1][1]))
    Max = max(Max, temp)

x = distance[0][0]
y = distance[0][1]
ans = 0
for i in range(1, n):
    ans += (abs(distance[i][0] - x) + abs(distance[i][1] - y))
    x = distance[i][0]
    y = distance[i][1]
print(ans - Max)