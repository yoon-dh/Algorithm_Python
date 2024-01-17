from heapq import *
import sys

input = sys.stdin.readline


def dijkstra(s):
    distance = [float('inf')] * (n + 1)
    hq = [[0, s]]
    distance[s] = 0
    while hq:
        t, x = heappop(hq)
        if distance[x] != t: continue
        for nx, nt in G[x]:
            if distance[nx] > t + nt:
                distance[nx] = t + nt
                heappush(hq, [distance[nx], nx])
    return distance


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans = [float('inf')] * (n + 1)
    G = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        G[a].append([b, c])
        G[b].append([a, c])
    k = int(input())
    friend = [*map(int, input().split())]
    for i in range(1, n + 1):
        dist = dijkstra(i)
        ans[i] = sum(dist[f] for f in friend)
    print(ans.index(min(ans)))
