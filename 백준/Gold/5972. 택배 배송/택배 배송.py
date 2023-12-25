import heapq

def dijkstra(G,start):
    distances = [int(1e9)] * (N + 1)
    distances[start] = 0
    Q = []
    heapq.heappush(Q,[distances[start],start])

    while Q:
        current_dist, current_node = heapq.heappop(Q)

        if distances[current_node] < current_dist: continue

        for next_node,next_dist in G[current_node]:
            distance_check = current_dist + next_dist
            if distances[next_node] > distance_check:
                distances[next_node] = distance_check
                heapq.heappush(Q,[distance_check,next_node])

    return distances

# ========================================

start = 1
N,M = map(int,input().split())
end = N

G = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,cost = map(int,input().split())
    G[s].append((e,cost))
    G[e].append((s,cost))

print(dijkstra(G,start)[end])

