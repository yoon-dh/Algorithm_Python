
import sys
input = sys.stdin.readline

S = input().rstrip()
P = input().rstrip()
p_idx = 0
ans = 0

while p_idx < len(P):
    Max, temp, s_idx = 0, 0, 0
    while s_idx < len(S) and p_idx + temp < len(P):
        if P[p_idx + temp] == S[s_idx]:
            temp += 1
            Max = max(Max, temp)
        else: temp = 0
        s_idx += 1
    p_idx += Max
    ans += 1
print(ans)