fibo = [0, 1]
for i in range(2, 50):
    fibo.append(fibo[i-2] + fibo[i-1])

T = int(input())
for j in range(T):
    n = int(input())
    arr = []

    while (n):
        for k in range(50):
            if (fibo[k] <= n):
                t = fibo[k]

        n -= t
        arr.append(t)
        arr.sort()

    print(*arr)