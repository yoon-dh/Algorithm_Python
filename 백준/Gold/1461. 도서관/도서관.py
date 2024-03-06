import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = sorted(map(int,input().split()))

minus = []
plus = []
Max = 0

for i in arr:
    if i < 0: minus.append(abs(i))
    else: plus.append(i)
    Max = max(Max,abs(i))

minus.sort(reverse=True)
plus.sort(reverse=True)

ans = 0
for i in range(0,len(plus),M):
    if plus[i] != Max: ans += plus[i] * 2

for i in range(0,len(minus),M):
    if minus[i] != Max: ans += minus[i] * 2

print(ans+Max)