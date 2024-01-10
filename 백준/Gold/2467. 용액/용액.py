def binary_search(s,e,current):
    global ans, left, right

    while s <= e:
        mid = (s + e) // 2
        temp = current + lst[mid]

        if abs(temp) < ans:
            ans = abs(temp)
            left = i
            right = mid

            if temp == 0:
                break

        if temp < 0: s = mid + 1
        else: e = mid - 1

# ========================================

n = int(input())
lst = list(map(int,input().split()))
ans = 0xffffffff
left = 0
right = 0

for i in range(n-1):
    current = lst[i]
    S = i + 1
    E = n - 1
    binary_search(S,E,current)

print(lst[left],lst[right])
