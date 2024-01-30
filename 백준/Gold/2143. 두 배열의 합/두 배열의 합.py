import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_sum_dict = defaultdict(int)
B_sum_dict = defaultdict(int)

for i in range(n):
    for j in range(i, n):
        A_sum_dict[sum(A[i:j+1])] += 1

for i in range(m):
    for j in range(i, m):
        B_sum_dict[sum(B[i:j+1])] += 1

ans = 0
for i in A_sum_dict.keys():
    ans += B_sum_dict[T - i] * A_sum_dict[i]
print(ans)