def count(lst):
    cnt = 1
    result = 1
    for i in range(1,n):
        if lst[i] == lst[i-1]:
            cnt += 1
            result = max(result,cnt)
        else:
            cnt = 1
    return result

def candy(arr):
    max_candy = 0
    for r in range(n-1):
        for c in range(n):
            arr[r][c], arr[r][c+1] = arr[r][c+1], arr[r][c]
            max_candy = max(max_candy,count(arr[r]))
            arr[r][c], arr[r][c+1] = arr[r][c+1], arr[r][c]

            arr[r][c], arr[r+1][c] = arr[r+1][c], arr[r][c]
            max_candy = max(max_candy, count(arr[r]),count(arr[r+1]))
            arr[r][c], arr[r+1][c] = arr[r+1][c], arr[r][c]

    return max_candy


n = int(input())
arr = [list(input()) + [0] for _ in range(n)] + [[0] *(n+1)]
arr_t = list(map(list,zip(*arr)))

print(max(candy(arr),candy(arr_t)))