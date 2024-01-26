from collections import deque
import sys
input = sys.stdin.readline

def square_num(x,y):
    return (x // 3) * 3 + (y // 3)

def backtrack(n):
        if n == blank_cnt:
            for i in arr:
                print(''.join(list(map(str, i))))
            return True

        current_x,current_y = Q.popleft()
        for i in range(1,10):
            if i not in row_arr[current_x] and i not in column_arr[current_y]:
                if i not in square_arr[square_num(current_x,current_y)]:
                    arr[current_x][current_y] = i
                    row_arr[current_x].add(i)
                    column_arr[current_y].add(i)
                    square_arr[square_num(current_x, current_y)].add(i)
                    if backtrack(n+1):
                        return True
                    arr[current_x][current_y] = 0
                    row_arr[current_x].discard(i)
                    column_arr[current_y].discard(i)
                    square_arr[square_num(current_x, current_y)].discard(i)
        Q.appendleft((current_x,current_y))

        return False

# =============================================

arr = [list(map(int,list(input().strip()))) for _ in range(9)]

row_arr = [set() for _ in range(9)]
column_arr = [set() for _ in range(9)]
square_arr = [set() for _ in range(9)]
Q = deque()

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0: Q.append((i,j))
        else:
            row_arr[i].add(arr[i][j])
            column_arr[j].add(arr[i][j])
            square_arr[square_num(i,j)].add(arr[i][j])

blank_cnt = len(Q)
backtrack(0)
