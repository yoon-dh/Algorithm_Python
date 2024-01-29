N = int(input())

nums = [1] * (N + 1)
for i in range(2, int(N ** 0.5) + 1):
    if nums[i]:
        for j in range(i + i, (N + 1), i):
            nums[j] = 0

e= 2
SUM = 0
cnt = 0
for i in range(2, N + 1):
    if nums[i] == 0: continue
    while SUM < N and e < N + 1:
        if not nums[e]:
            e += 1
            continue
        SUM += e
        e += 1
    if SUM == N: cnt += 1
    SUM -= i

print(cnt)