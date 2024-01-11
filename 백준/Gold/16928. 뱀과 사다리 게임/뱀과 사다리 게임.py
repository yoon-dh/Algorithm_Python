from collections import deque


N, M = map(int, input().split())
visited = [False for _ in range(101)]
jump = {}
for _ in range(N + M):
    tmp = list(map(int, input().split()))
    jump[tmp[0]] = tmp[1]

Q = deque([[1, 0]])  # 현재 위치, 주사위 굴린 횟수
visited[1] = True

while Q:
    v = Q.popleft()

    if v[0] == 100:
        print(v[1])
        exit()

    for i in range(1, 7):
        nv = v[0] + i

        if nv > 100:
            continue
        if visited[nv]:
            continue

        if nv in jump:
            nv = jump[nv]
            if not visited[nv]:
                visited[nv] = True
                Q.append([nv, v[1] + 1])
        else:
            visited[nv] = True
            Q.append([nv, v[1] + 1])