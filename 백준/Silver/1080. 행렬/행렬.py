def transform(i, j, A):
    for CI in range(i, i+3):
        for CJ in range(j, j+3):
            A[CI][CJ] = 1 - A[CI][CJ]

# =======================================================

N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]
ans = 0

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            ans += 1
            transform(i, j, A)

if A != B: print(-1)
else: print(ans)