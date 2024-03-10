n, m = map(int, input().split())
arr = [str(input()) for i in range(n)]

ans = ''
cnt = 0

for i in range(m):
    counting = [0, 0, 0, 0]

    for j in range(n):
        if arr[j][i] == 'A': counting[0] += 1
        elif arr[j][i] == 'C': counting[1] += 1
        elif arr[j][i] == 'G': counting[2] += 1
        elif arr[j][i] == 'T': counting[3] += 1

    idx = counting.index(max(counting))
    if idx == 0: ans += 'A'
    elif idx == 1: ans += 'C'
    elif idx == 2: ans += 'G'
    elif idx == 3: ans += 'T'

    cnt += n - max(counting)

print(ans)
print(cnt)
