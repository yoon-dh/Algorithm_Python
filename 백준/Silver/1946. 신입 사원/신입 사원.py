import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    rank = sorted([list(map(int, input().rstrip().split())) for _ in range(N)])
    cnt = 1
    S_rank = rank[0][1]
    for i in range(1,N):
        if rank[i][1] < S_rank:
            cnt += 1
            S_rank = rank[i][1]
    print(cnt)
