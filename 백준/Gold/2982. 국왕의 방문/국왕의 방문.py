import heapq
import sys


def dijkstra(S, E, TERM):
    INF = float('inf')
    distances = [INF] * (N + 1)
    distances[S] = TERM
    node_list = []
    heapq.heappush(node_list, (TERM, S))

    while node_list:
        current_time, current_node = heapq.heappop(node_list)

        for next_node in graph[current_node]:
            if time_spend_list.get((current_node, next_node)) and time_spend_list[(current_node, next_node)][0] <= current_time <= \
                    time_spend_list[(current_node, next_node)][1]:
                spend_time = time_spend_list[(current_node, next_node)][1] + graph[current_node][next_node]
            else:
                spend_time = current_time + graph[current_node][next_node]

            if distances[next_node] > spend_time:
                distances[next_node] = spend_time
                heapq.heappush(node_list, (spend_time, next_node))

    return distances

# ===============================================

input = sys.stdin.readline

N, M = map(int, input().split())

s, e, king_term, G = map(int, input().split())

king_visit_list = list(map(int, input().split()))

graph = [{} for _ in range(N + 1)]

for _ in range(M):
    x, y, times = map(int, input().split())

    graph[x][y] = min(graph[x].get(y, float('inf')), times)
    graph[y][x] = min(graph[y].get(x, float('inf')), times)

time_spend_list = {}

king_time = 0
for ind in range(G - 1):
    start, ends = king_visit_list[ind], king_visit_list[ind + 1]
    time_spend_list[(start, ends)] = (king_time, king_time + graph[start][ends])
    time_spend_list[(ends, start)] = (king_time, king_time + graph[start][ends])
    king_time += graph[start][ends]

result = dijkstra(s, e, king_term)

print(result[e] - king_term)