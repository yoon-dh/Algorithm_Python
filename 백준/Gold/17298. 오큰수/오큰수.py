n = int(input())
nums = list(map(int,input().split()))

Stack = []

answer = [-1] * (n)

for i in range(len(nums)):
    while len(Stack) != 0 and nums[Stack[-1]] < nums[i]:
        answer[Stack.pop()] = nums[i]
    Stack.append(i)


print(*answer)