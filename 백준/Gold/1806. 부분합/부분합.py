import sys
input = sys.stdin.readline

N,S = map(int,input().split())
lst = list(map(int,input().split()))
start_point = end_point = 0

Sum = lst[0]
ans = 100001

while True:
    if Sum < S:
        end_point += 1
        if end_point == N: break
        Sum += lst[end_point]
    else:
        Sum -= lst[start_point]
        ans = min(ans,end_point - start_point + 1)
        start_point += 1

if ans == 100001: print(0)
else: print(ans)