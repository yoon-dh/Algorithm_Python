import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distances[start] = 0
    while q:
        dist, current = heapq.heappop(q)

        if dist > distances[current]:
            continue

        for i in G[current]:
            distance = dist + i[1]
            if distance < distances[i[0]]:
                distances[i[0]] = distance
                heapq.heappush(q,(distance, i[0]))

    return distances[d]


n , d = map(int,input().split())
G = [[] for _ in range(d+1)]
distances = [int(1e9)] * (d+1)

for i in range(d):
    G[i].append((i+1, 1))


for _ in range(n):
    s, e, l = map(int,input().split())
    if e > d: continue
    G[s].append((e,l))

print(dijkstra(0))