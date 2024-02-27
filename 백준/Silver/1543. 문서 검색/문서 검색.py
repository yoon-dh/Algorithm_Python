from collections import Counter
import sys
input = sys.stdin.readline

S = input().rstrip()
target = input().rstrip()

while target in S:
    S = S.replace(target,'.')

C = Counter(S)
print(C['.'])