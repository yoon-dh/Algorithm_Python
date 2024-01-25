import sys
input = sys.stdin.readline

def backtracking(n, idx, current):
    if idx == input_number:
        ans = eval(current.replace(' ', ''))
        if ans == 0: result.append(current)
        return
    else:
        next_idx = idx + 1
        backtracking(n, next_idx, current + ' ' + str(next_idx))
        backtracking(n, next_idx, current + '+' + str(next_idx))
        backtracking(n, next_idx, current + '-' + str(next_idx))

T = int(input())
for _ in range(T):
    input_number = int(input())
    result = []
    backtracking(input_number, 1, '1')
    for a in result:
        print(a)
    print()