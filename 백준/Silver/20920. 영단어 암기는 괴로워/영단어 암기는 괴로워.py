import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
Dict = {}

for _ in range(N):
    S = input().rstrip()
    if len(S) < M: continue
    else:
        if S in Dict:  Dict[S] += 1
        else: Dict[S] = 1

Word = sorted(Dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))  # x[0] = 단어, x[1] = 단어 빈도수
for i in Word:
    print(i[0])