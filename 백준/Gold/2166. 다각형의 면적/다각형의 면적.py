import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append([*map(int, input().split())])

lst.append(lst[0])
P_cnt = 0
M_cnt = 0
for i in range(N):
    P_cnt += lst[i][0] * lst[i+1][1]
    M_cnt += lst[i][1] * lst[i+1][0]

ans = abs(P_cnt - M_cnt) / 2
print(round(ans,1))