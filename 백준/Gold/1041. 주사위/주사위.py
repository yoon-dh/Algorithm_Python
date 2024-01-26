import sys
input = sys.stdin.readline

n = int(input())
dice_lst = list(map(int, input().split()))
dice = []
dice.append(min(dice_lst[0], dice_lst[5]))
dice.append(min(dice_lst[1], dice_lst[4]))
dice.append(min(dice_lst[2], dice_lst[3]))
dice.sort()

ans = 0
if n == 1: ans += sum(dice_lst) - max(dice_lst)
else:
    for i in range(2):
        if i == 0: ans += (dice[0] * (n ** 2) + dice[1] * 4 * (n-1) + dice[2] * 4)
        else: ans += (dice[0] * 4 * (n-1) + dice[1] * 4) * (n-1)

print(ans)