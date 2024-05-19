import sys
input = sys.stdin.readline

def dfs(start, cnt):
    global ans
    if cnt == N // 2:
        A = 0
        for i in temp:
            for j in temp:
                A += arr[i][j]

        temp2 = []
        for i in range(N):
            if i in temp:
                continue
            temp2.append(i)

        B = 0
        for i in temp2:
            for j in temp2:
                B += arr[i][j]
        if abs(B - A) < ans:
            ans = abs(B - A)
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            temp.append(i)
            dfs(i + 1, cnt + 1)
            temp.pop()
            visited[i] = False

# ========================================================================

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

visited = [False for i in range(N)]
temp = []
ans = 0xffffffff

for k in range(0, N - 1):
    dfs(0, k)

print(ans)