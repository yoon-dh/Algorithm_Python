import sys,heapq
input = sys.stdin.readline

def dijkstra(start):
    distances = [int(1e9)] * (N + 1)
    q = []
    heapq.heappush(q,(0,start))
    distances[start] = 0
    while q:
        current_dist, current_node = heapq.heappop(q)
        if distances[current_node] < current_dist: continue

        for next_node, next_dist in G[current_node]:
            dist_sum = current_dist + next_dist
            if dist_sum < distances[next_node]:
                distances[next_node] = dist_sum
                heapq.heappush(q,(dist_sum,next_node))

    if start != X: distances_reverse[start] += distances[X]
    else: return distances

# ======================================

N,M,X = map(int,input().split())
G = [[] for _ in range(M+1)]

for _ in range(M):
    s,e,distance = map(int,input().split())
    G[s].append((e,distance))

distances_reverse = dijkstra(X)

for i in range(1,N+1):
    if i == X: continue
    dijkstra(i)

print(sorted(distances_reverse)[N-1])

