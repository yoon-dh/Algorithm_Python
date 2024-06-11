from itertools import combinations

N, M = map(int,input().split())
num_list = list(map(int,input().split()))

print(sorted([sum(i) for i in combinations(num_list,3) if sum(i) <= M])[-1])