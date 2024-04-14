def ccw():
    tmp = arr[0][0] * arr[1][1] + arr[1][0] * arr[2][1] + arr[2][0] * arr[0][1]
    tmp -= (arr[0][1] * arr[1][0] + arr[1][1] * arr[2][0] + arr[2][1] * arr[0][0])
    return tmp

# =================================================

arr = [list(map(int,input().split())) for _ in range(3)]
if ccw(): print("WINNER WINNER CHICKEN DINNER!")
else: print("WHERE IS MY CHICKEN?")

