import sys
input = sys.stdin.readline

n = int(input())

e = 0
ans = 0

arr = []
for i in range(0,n):
    a, b = map(int,input().rstrip().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0]))

for i, j in arr:
    if e <= i:
        ans += 1
        e = j
print(ans)