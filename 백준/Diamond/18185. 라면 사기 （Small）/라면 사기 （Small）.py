import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
visited = [0] * 100000

for i in range(n):
    visited[i] = lst[i]

money = 0

for i in range(n):
    if visited[i+1] <= visited[i+2]:
        min_ramen7 = min(visited[i],visited[i+1])
        money += min_ramen7 * 7
        visited[i] -= min_ramen7
        visited[i+1] -= min_ramen7
        visited[i+2] -= min_ramen7
    else:
        min_ramen5 = min(visited[i], visited[i+1] - visited[i+2])
        money += min_ramen5 * 5
        visited[i] -= min_ramen5
        visited[i+1] -= min_ramen5
        min_ramen7 = min(visited[i],visited[i+2])
        money += min_ramen7 * 7
        visited[i] -= min_ramen7
        visited[i+1] -= min_ramen7
        visited[i+2] -= min_ramen7


money += sum(visited) * 3
print(money)
