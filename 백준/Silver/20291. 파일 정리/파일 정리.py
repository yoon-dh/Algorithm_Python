import sys
input = sys.stdin.readline

n = int(input())

Dict = dict()
for _ in range(n):
    F,S = input().rstrip().split('.')
    if Dict.get(S) == None: Dict[S] = 1
    else: Dict[S] += 1

Dict_lst = sorted(Dict.items(),key = lambda x:x[0])
for i in Dict_lst:
    print(*i)