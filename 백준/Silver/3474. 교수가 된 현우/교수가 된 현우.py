import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    cnt = 0
    i = 5
    while i <= n:
        cnt += n // i
        i *= 5
    print(cnt)