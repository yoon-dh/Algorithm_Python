import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for v, w in G[now]:
            cost = d + w
            if cost < dist[v]:
                dist[v] = cost
                heapq.heappush(q, (cost, v))

V, E = map(int, input().split())
start = int(input())
INF = 1e9

dist = [INF] * (V + 1)
G = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

dijkstra(start)

for n in dist[1:]:
    print(n if n != INF else "INF")