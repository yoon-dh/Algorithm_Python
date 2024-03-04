import sys
input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0

if l == 1:
    print(len(lst))
    sys.exit()
while len(lst) != 0:
    temp = lst[0]
    cnt += 1
    for i in range(l):
        if temp + i in lst: lst.remove(temp + i)

print(cnt)