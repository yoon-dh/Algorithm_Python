from collections import deque
import sys
input = sys.stdin.readline

def BFS(s,e):
    Q = deque()
    Q.append((s,0))
    visited = [0] * (N+1)
    visited[s] = 1

    while Q:
        current_pos, total = Q.popleft()
        for next_pos,distance in G[current_pos]:
            if next_pos == e: return total + distance
            if not visited[next_pos]:
                visited[next_pos] = 1
                Q.append((next_pos,total + distance))
# ================================

N,M = map(int,input().split())
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    s,e,distance = map(int,input().split())
    G[s].append((e,distance))
    G[e].append((s,distance))

for _ in range(M):
    s,e = map(int,input().split())
    print(BFS(s,e))