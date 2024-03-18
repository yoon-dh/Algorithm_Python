import sys
input = sys.stdin.readline

def ZIP(arr):
    arr = zip(*arr[::-1])

    return [list(a) for a in arr]

def calc(arr):
    res = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j == 0: res += arr[i][j]
            else:
                if arr[i][j] > arr[i][j - 1]:
                    res += (arr[i][j] - arr[i][j-1])
    return res


n, m = map(int, input().split())
arr = []
res = 0

for i in range(n):
    arr.append(list(map(int, input().split())))
    res += len(arr[i])

res *= 2
copy_arr = arr

for i in range(4):
    res += calc(copy_arr)
    copy_arr = ZIP(copy_arr)

print(res)