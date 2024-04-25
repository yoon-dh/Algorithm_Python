
import sys
input = sys.stdin.readline

N = int(input())

arr = []
m = []
ans = 0
for _ in range(N):
    x = int(input())
    if x <= 0: m.append(x)
    elif x == 1: ans += 1
    else: arr.append(x)


m.sort()
arr.sort(reverse=True)

if len(arr) % 2 != 0: arr.append(1)
if len(m) % 2 != 0 : m.append(1)
for i in range(0, len(arr), 2): ans += (arr[i] * arr[i + 1])
for i in range(0, len(m), 2): ans += (m[i] * m[i + 1])

print(ans)