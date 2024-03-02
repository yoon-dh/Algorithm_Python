import heapq


def solution(N, road, K):
    dist = [int(1e9)]*(N+1) 
    dist[1] = 0  
    G = [[] for _ in range(N+1)]  
    for s,e,distance in road:
        G[s].append([distance,e])
        G[e].append([distance,s])
    
    hq = []
    heapq.heappush(hq, [0,1])
    while hq:
        current_cost, current_node = heapq.heappop(hq)
        for next_cost, next_node in G[current_node]:
            if current_cost + next_cost < dist[next_node]:
                dist[next_node] = current_cost + next_cost
                heapq.heappush(hq, [current_cost + next_cost, next_node])
                
    return len([i for i in dist if i <=K])
    