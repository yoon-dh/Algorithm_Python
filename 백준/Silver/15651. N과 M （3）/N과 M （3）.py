from itertools import product

n,m = map(int, input().split())
array = [list(range(1,n+1))]*m
xs = list(product(*array))

for x in xs:
    print(*x)