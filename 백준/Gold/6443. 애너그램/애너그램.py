import sys
input = sys.stdin.readline


def DFS(string, lst):
    if len(lst) == len(S):
        print(''.join(map(lambda x: chr(x + 97), lst)))
        return

    for idx in range(26):
        if string[idx] > 0:
            string[idx] -= 1
            lst.append(idx)
            DFS(string, lst)
            string[idx] += 1
            lst.pop()

# ==============================================

N = int(input())
for _ in range(N):
    S = input().strip()
    STR = [0] * 26
    for num in list(map(lambda x: x - 97, list(bytes(S, 'ascii')))):
        STR[num] += 1

    DFS(STR, [])

