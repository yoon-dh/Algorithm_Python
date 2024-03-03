arr = [[0]*100 for _ in range(100)]
n = int(input())

Sum = 0
for _ in range(n):
    r,c = map(int,input().split())

    for i in range(r,r+10):
        for j in range(c,c+10):
            if arr[i][j] == 0:
                arr[i][j] = 1
                Sum += 1

print(Sum)
