import sys
input = sys.stdin.readline

for t in range(int(input())):
    S = list(input().rstrip())
    i, j = 0, 1
    for idx in range(1, len(S)):
        if S[idx] > S[idx - 1]:
            if i < idx:
                i = idx

    for idx in range(1, len(S)):
        if S[idx] > S[i - 1]:
            if j < idx:
                j = idx

    if i != 0 and j != 0:
        S[i-1], S[j] = S[j], S[i-1]

        S[i:] = list(reversed(S[i:]))
    print(''.join(S))