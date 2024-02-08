import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

dict = {}
cnt = 0

for _ in range(N):
    dict[sys.stdin.readline().rstrip()] = 1
    cnt += 1

for _ in range(M):
    post = list(input().rstrip().split(','))
    for i in post:
        if i in dict.keys():
            if dict[i] == 1:
                dict[i] = 0
                cnt -= 1
    print(cnt)