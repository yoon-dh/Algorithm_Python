n = int(input())
sum = 0
ans = 0
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] == 1:
        sum += 1
        ans += sum
    else: sum = 0

print(ans)