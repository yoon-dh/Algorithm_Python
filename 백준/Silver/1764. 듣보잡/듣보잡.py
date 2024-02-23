import sys

N,M = map(int,sys.stdin.readline().split())

set_N = set([sys.stdin.readline().rstrip() for _ in range(N)])
set_M = set([sys.stdin.readline().rstrip() for _ in range(M)])
set_M_N = sorted(set_M & set_N)

print(len(set_M_N))
for i in set_M_N:
    print(i)