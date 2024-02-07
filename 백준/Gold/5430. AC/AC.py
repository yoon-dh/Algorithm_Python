T = int(input())
for _ in range(T):
    alpha = input()
    alpha = alpha.replace("RR", "")
    n = int(input())
    array = input()
    array = array[1:-1].split(",")

    front = back = 0  # 앞자리, 뒷자리 삭제
    reverse = 1  # 1이면 그대로,-1이면 reverse 
    for i in alpha:
        if i == 'R':
            reverse *= -1
        elif i == 'D':
            if reverse == 1:
                front += 1
            else:
                back += 1

    if front + back <= n:
        array = array[front:n - back]
        if reverse == 1:
            print('[' + ','.join(array) + ']')
        else:
            print('[' + ','.join(array[::-1]) + ']')
    else:
        print('error')