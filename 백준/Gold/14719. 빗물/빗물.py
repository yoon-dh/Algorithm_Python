H,W = map(int,input().split())

row = list(map(int,input().split()))

ans = 0

for i in range(1,W-1):
    left_max = max(row[:i])
    right_max = max(row[i+1:])

    compare = min(left_max,right_max)

    if row[i] < compare:
        ans += compare - row[i]

print(ans)