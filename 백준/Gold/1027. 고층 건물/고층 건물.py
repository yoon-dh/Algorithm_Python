N = int(input())
arr = list(map(int, input().split()))
ans = 0

for i in range(N):
    temp = N - 1
    for j in range(i + 1, N):
        for k in range(i + 1, j):
            if arr[k] - arr[i] >= (((arr[j] - arr[i]) / (j - i)) * (k - i)):
                temp -= 1
                break

    for j in range(0, i):
        for k in range(j + 1, i):
            if arr[k] - arr[j] >= (((arr[i] - arr[j]) / (i - j)) * (k - j)):
                temp -= 1
                break
        
    ans = max(temp, ans)
print(ans)