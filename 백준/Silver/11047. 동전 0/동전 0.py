import sys

n, k = map(int,sys.stdin.readline().split())

kind = sorted([int(sys.stdin.readline()) for i in range(n)],reverse=True)

cnt = 0

for i in range(len(kind)):
    cnt += k//kind[i]
    k %= kind[i]

print(cnt)