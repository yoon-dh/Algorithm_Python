N = int(input())
A = list(map(int, input().split()))   

result =0

for i in A :
    cnt = 0
    for j in range(2, i+1) :
        if i%j == 0 :
            cnt += 1
    if cnt == 1 :
        result += 1

print(result)