S = list(input())
T = list(input())

while True:
    if S == T:
        print(1)
        break
    if len(T) == 0:
        print(0)
        break

    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]
    else:
        print(0)
        break
