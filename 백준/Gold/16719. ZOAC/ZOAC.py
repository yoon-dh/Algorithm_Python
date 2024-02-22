import sys
input = sys.stdin.readline


def DFS(S, start):
    global result

    if S == "": return

    Min = min(S)
    Min_idx = S.index(Min)
    ans[start + Min_idx] = Min

    print(''.join(ans))

    DFS(S[Min_idx + 1:], start + Min_idx + 1)
    DFS(S[:Min_idx], start)

# ============================================

S = input().rstrip()
ans = [''] * len(S)
DFS(S, 0)