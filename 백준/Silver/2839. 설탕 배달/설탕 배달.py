import sys

read = sys.stdin.readline
N = int(read())

arr = [5001] * (N+5)
arr[3] = arr[5] = 1

for i in range(6, N+1):
    arr[i] = min(arr[i-3], arr[i-5]) + 1

print(arr[N] if arr[N] < 5001 else -1)