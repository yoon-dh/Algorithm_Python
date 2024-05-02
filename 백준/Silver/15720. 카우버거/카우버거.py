import sys
input = sys.stdin.readline

B, C, D = map(int, input().rstrip().split())

B_lst = sorted(map(int, input().split()), reverse=True)
C_lst = sorted(map(int, input().split()), reverse=True)
D_lst = sorted(map(int, input().split()), reverse=True)

before_ans = sum(B_lst) + sum(C_lst) + sum(D_lst)

cnt = min(len(B_lst), len(C_lst), len(D_lst))
set_ans = before_ans - (sum(B_lst[:cnt]) + sum(C_lst[:cnt]) + sum(D_lst[:cnt])) // 10

print(before_ans)
print(set_ans)