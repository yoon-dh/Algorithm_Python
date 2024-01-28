import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
ans = [0]

for i in lst:
    if ans[-1]<i:
        ans.append(i)
    else:
        s = 0
        e = len(ans)

        while s < e:
            mid = (s + e)//2
            if ans[mid] < i:
                s = mid + 1
            else:
                e = mid
        ans[e] = i

print(len(ans)-1)
