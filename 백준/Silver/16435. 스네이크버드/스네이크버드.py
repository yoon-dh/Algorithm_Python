N,L = map(int,input().split())
lst = sorted(map(int,input().split()))

for i in lst:
    if i <= L:
        L += 1
print(L)